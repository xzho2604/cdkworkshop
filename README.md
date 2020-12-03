

## Why CDK
* infrastructure as code
  * component reusability, portablity
  * version control, roll back to the previous verisoin
  * clean code architecture, rather than file based

## file structure
```shell
├── README.md
├── app.py
├── cdk.json
├── cdk.out
│   ├── asset.37966b8a9595e568ac5e3e185e2f1cff2f2959574d66a95e92dcfae7b6761931
│   │   └── hello.py
│   ├── cdk.out
│   ├── cdkworkshop.template.json
│   ├── manifest.json
│   └── tree.json
├── cdkworkshop
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── __init__.cpython-39.pyc
│   │   ├── cdkworkshop_stack.cpython-38.pyc
│   │   └── cdkworkshop_stack.cpython-39.pyc
│   ├── cdkworkshop.egg-info
│   │   ├── PKG-INFO
│   │   ├── SOURCES.txt
│   │   ├── dependency_links.txt
│   │   ├── requires.txt
│   │   └── top_level.txt
│   └── cdkworkshop_stack.py
├── hitcounter.py
├── lambda
│   ├── hello.py
│   └── hitcount.py
├── requirements.txt
├── setup.py
├── source.bat
└── tests
    ├── __init__.py
    └── unit
        ├── __init__.py
        └── test_cdkworkshop_stack.py

```
### Architeucture
![](image/aws_graph.png)

## code structure
### Constructor
* level 1: beginning with low-level constructs, These constructs directly represent all resources available in AWS CloudFormation
```pytyhon
bucket = s3.CfnBucket(self, "MyBucket", bucket_name="MyBucket")
```
* level 2: The next level of constructs, L2, also represent AWS resources, but with a higher-level, intent-based API
  * They provide similar functionality, but provide the defaults, boilerplate, and glue logic you'd be writing yourself with a CFN Resource construct.
  * AWS constructs offer convenient defaults and reduce the need to know all the details about the AWS resources they represent, while providing convenience methods that make it simpler to work with the resource.

### path
*  We refer to the collection of IDs from a given construct, its parent construct, its grandparent, and so on to the root of the construct tree, as a path

### Token
* Tokens are objects that implement the IResolvable interface, which contains a single resolve method.
* The AWS CDK calls this method during synthesis to produce the final value for the AWS CloudFormation template

## commands
* cdk ls
* cdk synth
* cdk bootstrap: when have to use bootstrap
* cdk deploy
* cdk diff


## Test the HitCounter
```shell
curl https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/prod/
curl https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/prod/
curl https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/prod/hello
curl https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/prod/hello/world
curl https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/prod/hello/world
```

## Using DB table viewer
```shell
python -m pip install cdk-dynamo-table-viewer  
```

## Resources
* [cdk workskhop](https://cdkworkshop.com/)
* [cdk developer guide](https://docs.aws.amazon.com/cdk/latest/guide/home.html)

