Usage
=====

The **aws_simple_pipeline** package reads the file named **buildspec.yml** that it finds in the same directory of **app.py** file, where you have to initialize its PipelineStack class.

You can describe all steps that you need, directly in the **buildspec.yml** file, or you can run an external script for each step, that you can test it on your client.

You have to manage a git token in **app.py**, and you can create it by `AWS console <https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html>`_ or `aws-cli <https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/create-secret.html>`_:

.. code-block:: bash

    aws secretsmanager create-secret \
        --name /aws-simple-pipeline/secrets/github/token \
        --secret-string '{"github-token":"YOUR_TOKEN"}'

There are many methods for creating a secret object because it can be replicated automatically,
but it is not the purpose of this guide. Now, we only need to create it once for all our implementations.

Example
#######

You need to create the infrastructure of your `aws-saving <https://github.com/bilardi/aws-saving/>`_ solution for

* your test, because you want to improve a feature
* a CI/CD system, because you want to use **aws-saving** solution on your AWS account

For the Continuous Integration (CI)
***********************************

You can use some bash scripts for testing each step

* **local.sh**, for running all bash scripts with one command
* **build.sh**, for loading all requirements
* **unit_test.sh**, for testing the code
* **deploy.sh**, for deploying on AWS account the infrastructure of your **aws-saving** solution
* **integration_test.sh**, for testing the resources integration

For the CD system
*****************

You have to use the files **app.py** and **buildspec.yml**

* CD is Continuous Delivery, if you set ``manual_approval_exists = True`` on the file **app.py**
* CD is Continuous Deployment, if you set ``manual_approval_exists = False`` on the file **app.py**

You can save the **buildspec.yml** file in the same directory of **app.py** file,
and it will be loaded without defining anything.

Or you can also save it in another folder,

* you have to set ``buildspec_path = 'relative/path/from/repo/root/buildspec.yml'`` on the file **app.py**
* you can find some examples on the follow repositories

  * `aws-tool-comparison/cdk/python/app.py <https://github.com/bilardi/aws-tool-comparison/tree/master/cdk/python/app.py>`_, where the buildspec_path is defined
  * `aws-static-gui-resources/app_pipeline.py <https://github.com/bilardi/aws-static-gui-resources/tree/master/app_pipeline.py>`_, where the buildspec_path is not defined because it is the default

For managing many environments in parallel
******************************************

If you use the command ``cdk deploy``, you will create a pipeline with that project name with two environments: one named **staging** and one named **production**.

But if you need to manage more environments, like for my-development, your-development, and so on, you can use at least two methods:

* you can use the command ``cdk deploy -c stage=my-development``, as described in :ref:`Development section <Development>`
* or you can use the property **stage** at the initialization, as used in `aws-static-gui-resources <https://github.com/bilardi/aws-static-gui-resources/tree/master/app_pipeline.py>`_ where the stage is the branch name
