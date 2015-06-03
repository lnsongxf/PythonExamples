import boto.ec2

connEC2 = boto.ec2.connect_to_region("us-east-1")
connEC2.get_all_instances()

connEC2.get_all_key_pairs()
sgroup_rules = [print(sgroup.rules) for sgroup in
                connEC2.get_all_security_groups()]