# Tidy phoneme categorization task --------------------------------------------
#
# Last update: 2021-10-24
# Read and tidy raw data from pilot phoneme cat task
# - participants heard 5x of 4 vowels
# - they chose which English or Spanish vowel was the closest fit
# - they rate there choice 
# -----------------------------------------------------------------------------

# Source libs -----------------------------------------------------------------

source(here::here("scripts", "perception", "00_libs.R"))

# -----------------------------------------------------------------------------



pct_data <- dir_ls(here("data", "raw", "pct"), regexp = "\\.csv$") %>%
  map_dfr(read_csv, .id = "source", col_types = cols(.default = "c")) %>% 
  filter(!is.na(date)) 

# find prolific ids of those who completed the task and added their id
prol_id_df <- pct_data %>% 
  group_by(participant) %>% 
  summarise(done = n()) %>% 
  filter(!is.na(participant)) %>% 
  filter(done == 23)

# get the ones who didn't add id 
dates_df <- pct_data %>% 
  filter(is.na(participant)) %>% 
  group_by(date) %>% 
  summarise(done = n()) %>% 
  filter(done == 23)

# subset main dataframe to add separate the non-id people and give them
# an id, re-bind it all 

tidy_data_id <- pct_data %>% 
  filter(participant %in% prol_id_df$participant) 

tidy_data_no_id <- pct_data %>% 
  filter(date %in% dates_df$date) %>% 
  mutate(participant = case_when(date == dates_df$date[1] ~ "noid1",
                                 date == dates_df$date[2] ~ "noid2",
                                 date == dates_df$date[3] ~ "noid3",
                                 date == dates_df$date[4] ~ "noid4",
                                 date == dates_df$date[5] ~ "noid5",
                                 date == dates_df$date[6] ~ "noid6"))
tidy_data_id %>% 
  group_by(participant) %>% 
  summarise(done = n()) 


tidy_df <- rbind(tidy_data_id, tidy_data_no_id)

tidy_df %>% 
  write.csv(here("data", "tidy", "pct", "pct_tidy.csv"))



