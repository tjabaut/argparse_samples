# AWS Account and VPC
#     show-compatible-subnets [LINKEDACCOUNTID] [REGION]: show compatible native AWS subnets connected to the SDDC")
#     show-connected-accounts: show native AWS accounts connected to the SDDC")
#     show-sddc-connected-vpc: show the VPC connected to the SDDC")
#     show-shadow-account: show the Shadow AWS Account VMC is deployed in\n")
# SDDC
#     get-access-token: show your access token")
#     show-sddc-state: get a view of your selected SDDC")
#     show-sddcs: display a lit of your SDDCs")
#     show-vms: get a list of your VMs\n")
# TKG
#     enable-tkg: Enable Tanzu Kubernetes Grid on an SDDC")
#     disable-tkg: Disable Tanzu Kubernetes Grid on an SDDC\n")

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("get-access-token", help="show your access token")
parser.add_argument("show-sddc-state", help="get a view of your selected SDDC")
parser.add_argument("show-sddcs", help="display a lit of your SDDCs")
parser.add_argument("show-vms", help="get a list of your VMs")
# parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2], help="increase output verbosity")
args = parser.parse_args()
# print(vars(args))
# answer = args.square**2
# # print(answer)
# if args.verbosity == 2:
#     print(f"the square of {args.square} equals {answer}")
# elif args.verbosity == 1:
#     print(f"{args.square}^2 == {answer}")
# else:
#     print(answer)
