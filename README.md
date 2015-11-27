# cnr_lease_parser

./nrcmd -b "scope SCOPENAME listLeases" > leases

python ./cnr_lease_parser.py --file leases --date Dec,3 > parsed_leases
