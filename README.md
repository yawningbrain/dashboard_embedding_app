# AI/BI Dashboard App on Flask

This is a Flask app that embeds an AI/BI dashboard and can run inside a Databricks cluster.

## Running Locally
\`\`\`bash
pip install -r requirements.txt
python run.py
\`\`\`

## Deploying in Databricks

- Upload the entire folder to DBFS or attach it as a workspace directory.
- Use \`dbutils.notebook.run\` or \`%run ./run\` in a notebook.
- Ensure Flask runs in the notebook output (or deploy using \`ngrok\`/proxy setup).
