import db_config



list_file_name = 'all_brands_list.txt'
all_info_name = 'all_info.json'
model_list_file = 'all_model_list.txt'
main_url = 'http://www.gsmarena.com/'
base_url = "http://www.gsmarena.com/makers.php3"
all_images_folder = 'all_images'
all_data_name = 'all_data'
possibleImageExtensions = ['.jpg','.gif']
dateTimeFormat = '%Y-%m-%d-%H-%M-%S'
wamp_mysql_path_dir = 'C:\\wamp\\bin\\mysql\\mysql5.6.17\\bin'
db_back_up_dir = 'D:\\qt_projects\\webty\\db_backup'
db_string_separator = '*****'

loader_image_name = 'loader.gif'

unwanted_imagename_chars = ['/', '\\', '*',':)']

def remove_unwanted_chars_in_string(string_val):
    for a in unwanted_imagename_chars:
        if a in string_val:
            string_val = string_val.replace(a,'_')
    return string_val

#***************************** SQL STATEMENTS*******************************************
#login
databaseName = db_config.databaseName
databaseHostName = db_config.databaseHostName
databaseUserName = db_config.databaseUserName
databasePassword=db_config.databasePassword

# all table names
staffTableName = 'staff'
phonesTableName = 'phones'
customersTableName = 'customers'
repairJobsTableName = 'repairjobs'
sparePartsTableName = 'spareparts'
smsAccTableName = 'smsaccounts'
fixedTableName = 'fixedItems'
moneyTableName = 'money'
activityTableName = 'activitylog'
webtyprefsTableName = 'webtyprefs'


allid_column = '_id'
date_added_column = 'date_added'
#columns
#phone_columns
phone_name_column = 'phone_name'
phone_pic_location_column = 'phone_pic_location'
phone_page_link_column = 'phone_page_link'
phone_extra_info_column = 'phone_extra_info'
#staff columns
staff_name = 'staff_name'
staff_username_column='staff_username'
staff_password_column = 'staff_password'
staff_designation_column = 'staff_designation'
staff_smscredit_column = 'staff_smscredit'
#customer columns
customer_name_column = 'customer_name'
customer_phone_number_column = 'customer_phone_number'
customer_other_number_column = 'customer_other_number'
customer_date_receieved_column = 'date_added'
#repair columns
repair_job_item_name = 'jobs_item'
repair_job_customer_id = 'jobs_customer_id'
repair_job_bill='jobs_bill'
repair_job_bill_paid='jobs_bill_paid'
repair_job_status='jobs_status'
repair_job_date_received='jobs_date_received'
repair_job_date_returned='jobs_date_returned'
repair_job_other_info='jobs_other_info'
repair_job_imei_serial = 'jobs_imei_serial'
repair_job_knownfaults = 'jobs_known_faults'
repair_job_customer_notified = 'jobs_customer_notified'
#spareparts columns
spareparts_name_column = 'spare_name'
spareparts_price_column = 'spare_price'
spare_quantity_column = 'spare_quantity'
spare_vendor_column = 'spare_vendor'
#sms columns
sms_username_column = 'sms_username'
sms_password_column = 'sms_password'
sms_balance_column = 'sms_balance'
sms_check_balance_column = 'sms_check_balance'
sms_active_column = 'sms_active'
sms_sender_id = 'sms_sender_id'
sms_send_url_column = 'sms_send_url'
#money columns
money_amount_column = 'money_amount'
money_transact_type_column = 'money_transact_type'
money_repairjob_id_column = 'money_repairjob_id'
money_other_info_column = 'money_other_info'
money_medium_column = 'money_medium'
#log column
activity_staff_column = 'activity_staff'
activity_info_column = 'activity_info'
# webtyprefs columns
webtyprefs_item_column = 'webtypref_item'
webtyprefs_info_column = 'webtypref_info'
# webtyprefs items
webtyprefs_item_fixed_sms = 'fixed_item_sms'
webtyprefs_item_timestamp = 'time_stamp'





#create database
createDatabase = "CREATE DATABASE IF NOT EXISTS %s;" %databaseName

#creat tables
createPhonesTable = "CREATE TABLE IF NOT EXISTS phones" \
                    "(_id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT," \
                    "phone_name VARCHAR(255) NOT NULL," \
                    "phone_pic_location VARCHAR(255) NOT NULL," \
                    "phone_page_link VARCHAR(255) NOT NULL," \
                    "phone_extra_info TEXT NOT NULL," \
                    "date_added DATETIME NOT NULL);"


createStaffTable = "CREATE TABLE IF NOT EXISTS staff" \
                   "(_id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT," \
                   "staff_name VARCHAR(255) NOT NULL," \
                   "staff_username VARCHAR(255) NOT NULL," \
                   "staff_password VARCHAR(255) NOT NULL," \
                   "staff_designation VARCHAR(255) NOT NULL," \
                   "staff_smscredit VARCHAR (255) NOT NULL," \
                   "date_added DATETIME NOT NULL);"

createCustomerTable = "CREATE TABLE IF NOT EXISTS customers" \
                      "(_id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT," \
                      "customer_name VARCHAR(255) NOT NULL," \
                      "customer_phone_number VARCHAR(255) NOT NULL," \
                      "customer_other_number VARCHAR (255)NOT NULL," \
                      "date_added DATETIME NOT NULL);"

createRepairJobsTable = "CREATE TABLE IF NOT EXISTS repairjobs " \
                        "(_id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT," \
                        "jobs_item VARCHAR(255) NOT NULL," \
                        "jobs_customer_id VARCHAR (255) NOT NULL," \
                        "jobs_bill VARCHAR (255) NOT NULL," \
                        "jobs_other_info TEXT NOT NULL," \
                        "jobs_bill_paid VARCHAR(255) NOT NULL," \
                        "jobs_status VARCHAR(255) NOT NULL," \
                        "jobs_date_received DATETIME NOT NULL," \
                        "jobs_date_returned DATETIME NOT NULL," \
                        "jobs_imei_serial VARCHAR(255) NOT NULL," \
                        "jobs_known_faults VARCHAR (255) NOT NULL," \
                        "jobs_customer_notified VARCHAR (255) DEFAULT 0 NOT NULL);"

createSparePartsTable = "CREATE TABLE IF NOT EXISTS spareparts " \
                        "(_id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT," \
                        "spare_name VARCHAR(255) NOT NULL," \
                        "spare_price VARCHAR(255) NOT NULL," \
                        "spare_quantity VARCHAR(255) NOT NULL," \
                        "spare_vendor VARCHAR (255) NOT NULL," \
                        "date_added DATETIME NOT NULL);"

createSmsTable = "CREATE TABLE IF NOT EXISTS smsaccounts " \
                 "(_id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT," \
                 "sms_username VARCHAR(255) NOT NULL," \
                 "sms_password VARCHAR (255) NOT NULL," \
                 "sms_balance VARCHAR(255) NOT NULL," \
                 "sms_check_balance VARCHAR(255) NOT NULL," \
                 "sms_active VARCHAR (255) NOT NULL," \
                 "sms_sender_id VARCHAR (255) NOT NULL," \
                 "sms_send_url VARCHAR (255) NOT NULL," \
                 "date_added DATETIME NOT NULL);"

createTransactionTable = "CREATE TABLE IF NOT EXISTS money " \
                 "(_id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT," \
                 "money_amount VARCHAR(255) NOT NULL," \
                 "money_transact_type VARCHAR (255) NOT NULL," \
                 "money_repairjob_id VARCHAR(255) NOT NULL," \
                 "money_other_info VARCHAR(255) NOT NULL," \
                 "money_medium VARCHAR (255) NOT NULL," \
                 "date_added DATETIME NOT NULL);"

createLogTable = "CREATE TABLE IF NOT EXISTS activitylog " \
                 "(_id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT," \
                 "activity_staff VARCHAR(255) NOT NULL," \
                 "activity_info VARCHAR (255) NOT NULL," \
                 "date_added DATETIME NOT NULL);"

createPrefsTable = "CREATE TABLE IF NOT EXISTS webtyprefs " \
                 "(_id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT," \
                 "webtypref_item VARCHAR(255) NOT NULL," \
                 "webtypref_info VARCHAR (255) NOT NULL," \
                 "date_added DATETIME NOT NULL);"

