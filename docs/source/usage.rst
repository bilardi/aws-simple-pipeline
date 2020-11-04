Usage
=====

The **aws_simple_pipeline** package reads the file named **buildspec.yml** that it finds in the same directory of **app.py** file, where you have to initialize its PipelineStack class.

You can describe all steps that you need, directly in the **buildspec.yml** file, or you can run an external script for each step, that you can test it on your client.

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

You have to save the **buildspec.yml** file in the same directory of **app.py** file.
