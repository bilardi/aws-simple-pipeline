from aws_cdk import core
from aws_simple_pipeline.pipeline_stack import PipelineStack
from aws_cdk_test_synth.test_synth import TestSynth

class TestPipelineStack(TestSynth):
    manual_approval = None
    token = None

    def __init__(self, *args, **kwargs):
        self.token = core.SecretValue.secrets_manager(
            "/aws-simple-pipeline/secrets/github/token",
            json_field='github-token',
        )
        TestSynth.__init__(self, 'tests/pipeline_stack_with_manual_approval_false.yaml', *args, **kwargs)

    def synth(self, app):
        PipelineStack(app, 
            id="test",
            github_owner="owner",
            github_repo="repo",
            github_branch="branch",
            github_token=self.token,
            notify_emails=["email"],
            policies=["policy"]
        )

    def synth_with_manual_approval(self, app):
        PipelineStack(app, 
            id="test",
            github_owner="owner",
            github_repo="repo",
            github_branch="branch",
            github_token=self.token,
            notify_emails=["email"],
            policies=["policy"],
            manual_approval_exists=self.manual_approval
        )

    def test_synth_with_manual_approval_true(self):
        self.manual_approval = True
        self.load_template('tests/pipeline_stack_with_manual_approval_true.yaml')
        self.synthesizes('synth_with_manual_approval')

    def test_synth_with_manual_approval_false(self):
        self.manual_approval = False
        self.load_template('tests/pipeline_stack_with_manual_approval_false.yaml')
        self.synthesizes('synth_with_manual_approval')

if __name__ == '__main__':
    unittest.main()
