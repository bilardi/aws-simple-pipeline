#!/usr/bin/env python3

from aws_cdk import core
from aws_simple_pipeline.pipeline_stack import PipelineStack

project_name = "aws-simple-pipeline"
github_owner = "bilardi"
github_repo = "aws-simple-pipeline"
github_branch = "master"
github_token = core.SecretValue.secrets_manager(
    "/aws-simple-pipeline/secrets/github/token",
    json_field='github-token',
)
notify_emails = [ "your@email.net" ]
policies = [
    # "AdministratorAccess", # avoid in production
    "AWSLambda_FullAccess",
    "AWSCloudFormationFullAccess",
    "CloudWatchLogsFullAccess",
    "CloudWatchEventsFullAccess",
    "AmazonS3FullAccess",
    "IAMFullAccess",
]
# buildspec_path = "buildspec.yml"
manual_approval_exists = True

app = core.App()
# stage = app.node.try_get_context("stage")
PipelineStack(app, 
    id=project_name,
#    stage=stage,
    github_owner=github_owner,
    github_repo=github_repo,
    github_branch=github_branch,
    github_token=github_token,
    notify_emails=notify_emails,
    policies=policies,
#    buildspec_path=buildspec_path,
    manual_approval_exists=manual_approval_exists
)

app.synth()
