# ------------------------------------------------------
# Author: Kyle Parrish
# Date 5/2/22
# A script to load data - it is typically run by other scripts 
#
# -------------------------------------------------------


pct_tidy = read.csv(here::here("data", "perception", "tidy", "pct_tidy.csv"))

pct_tidy_mono = read.csv(here("data", "perception", "tidy", "tidy_mono_groups.csv"))

pct_eng_mono = pct_tidy_mono %>% 
  filter(L1 == "English_mono")

length(unique(pct_eng_mono$participant))

pct_span_mono = pct_tidy_mono %>% 
  filter(L1 == "Spanish_mono")

length(unique(pct_span_mono$participant))

span_blp = read.csv(here("data", "perception", "tidy", "span_l1_blp.csv"))
eng_blp = read.csv(here("data", "perception", "tidy", "eng_l1_blp.csv"))

removed = read.csv(here("data", "perception", "tidy", "removed.csv"))

english_l1_pct = pct_tidy %>% 
  filter(L1 == "English") %>% 
  filter(participant %in% eng_blp$prolific_id)

english_l1_pct_g = pct_tidy %>% 
  filter(L1 == "English") %>% 
  filter(stim_language == "German") %>% 
  filter(participant %in% eng_blp$prolific_id)

spanish_l1_pct = pct_tidy %>% 
  #  filter(L1 == "Spanish") %>% 
  filter(stim_language == "french") %>% 
  filter(participant %in% span_blp$prolific_id)

spanish_l1_pct_g = pct_tidy %>% 
  filter(L1 == "Spanish") %>% 
  filter(stim_language == "German") %>% 
  filter(participant %in% span_blp$prolific_id)



cond_df_prob = read.csv(here("data", "perception", "tidy", "cond_prob_df.csv"))

eng_cond_df_comb = read.csv(here("data", "perception", "tidy", "eng_cond_df_comb.csv"))

sp_cond_df_comb = read.csv(here("data", "perception", "tidy", "span_cond_df_comb.csv"))



