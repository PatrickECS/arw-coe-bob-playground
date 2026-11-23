# Bob: read-only access to the lab clusters (MCP) and skills

Gives Bob read-only access to all lab OpenShift clusters through the `openshift-lab` MCP server, using a personal token, plus three skills:

- `lab-health-check`: health checks and troubleshooting for the lab clusters.
- `fusion-health-check`: a detailed health check of the IBM Fusion HCI system isf.
- `fusion-hci-systems`: IBM Fusion HCI 2.13 / 2.14 product knowledge.

**You need:** admin access to isf, `oc`, `jq` and `git` on your Mac, access to the `patrik-bob` Git repository, and a working Bob setup (IdM CA trusted).

## 1. Log in to isf

Log in as admin the way you normally do, then check you are on isf:

```bash
oc whoami --show-server
```

## 2. Create your token and add the MCP server to Bob

Set `NAME` to your IdM username (lowercase), then paste the whole block. The token is never shown.

```bash
NAME=anna
oc create sa mcp-$NAME -n bob-mcp
oc create rolebinding mcp-$NAME -n bob-mcp --role=bob-mcp-user --serviceaccount=bob-mcp:mcp-$NAME
oc apply -n bob-mcp -f - <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: mcp-$NAME-token
  annotations:
    kubernetes.io/service-account.name: mcp-$NAME
type: kubernetes.io/service-account-token
EOF
sleep 3
TOKEN=$(oc get secret mcp-$NAME-token -n bob-mcp -o jsonpath='{.data.token}' | base64 -d)
f=~/.bob/settings/mcp.json
mkdir -p ~/.bob/settings
[ -f "$f" ] || echo '{"mcpServers":{}}' > "$f"
jq --arg t "$TOKEN" '.mcpServers["openshift-lab"] = {type: "streamable-http", url: "https://bob-mcp-bob-mcp.apps.isf.eu.arrow.lab/mcp", headers: {Authorization: ("Bearer " + $t)}}' "$f" > "$f.tmp" && mv "$f.tmp" "$f"
chmod 600 "$f"
unset TOKEN
```

## 3. Add the skills to Bob

Set `REPO` to the folder you cloned the repository into, then paste the rest. It copies each skill folder from `$REPO/projects/bob/skills/cluster-overview` into Bob's skills folder.

```bash
git clone <repo-url>
REPO=~/patrik-bob
ls "$REPO/projects/bob/skills/cluster-overview"
mkdir -p ~/.bob/skills
cp -R "$REPO"/projects/bob/skills/cluster-overview/* ~/.bob/skills/
ls ~/.bob/skills/
```

The first `ls` should list `fusion-hci-systems`, `fusion-health-check` and `lab-health-check`. The last `ls` should show the same three folders in Bob's skills folder.

Each skill must stay in its own folder, with the folder name unchanged. Bob skips a skill if its folder name does not match the `name:` line in its `SKILL.md`.

**To update the skills later:**

```bash
REPO=~/code/patrik-bob
git -C "$REPO" pull
cp -R "$REPO"/projects/bob/skills/cluster-overview/* ~/.bob/skills/
```

## 4. Restart Bob and test

Quit Bob with Cmd+Q and reopen it. Check:

- In the MCP settings, `openshift-lab` shows as connected.
- Under **Bob Settings → Skills**, `lab-health-check`, `fusion-health-check` and `fusion-hci-systems` are listed.

Then try, each in a new chat:

- *"Which clusters can you access?"*
- *"Display the health status of the Fusion HCI system called isf."* Bob answers in rounds. Reply *continue* to get the next round.
- *"What's wrong with wxai?"*
- *"What's new in Fusion HCI 2.14?"*

If Bob does not pick the right skill, start the question with the skill name, for example `/fusion-health-check`.

## Rules

- The token gives read access to every lab cluster. Treat it like a password.
- Only use it with our self-hosted Bob. Never with `bob.ibm.com` or other AI tools.
- The `fusion-hci-systems` skill is for internal use. Do not share it outside Arrow.

## Remove your access

Logged in to isf, with `NAME` set to your username:

```bash
NAME=anna
oc delete sa mcp-$NAME -n bob-mcp
oc delete rolebinding mcp-$NAME -n bob-mcp
```