# Tidy phoneme categorization task in French ----------------------
#
# Source libs -----------------------------------------------------------------

source(here::here("scripts", "perception", "00_libs.R"))

# -----------------------------------------------------------------------------



stim_list = c(
  "stim/pof_f.wav",
  "stim/pif_f.wav",
  "stim/peuf_f.wav",
  "stim/p_schwa_f.wav",
  "stim/fof_f.wav",
  "stim/fif_f.wav",
  "stim/feuf_f.wav",
  "stim/f_schwa_f.wav")

participants_done = 
c("6124d122d91be3f612508804",
"5f9057735c69b00e72665f84",
"5bcc60b95c2b810001dc68e2",
"59349d79f1b3f00001964d04",
"5c2fae74d76cde0001c11590",
"6125b040ffa3c0b9e67b92c9",
"5898b6e256357700011c2c6b",
"5dc483cf74939e34e55c3619",
"60e1d5f866e681d7e33fd01c",
"5ffe6b8b773ec452c1d28adc",
"5e27868c5cbbcc0b3599574b",
"5ef9df1812148a78af8e76dc",
"5fb0a3d6a8e4224b973e750b",
"5ff5f7ad932d56101bf7c90d",
"60121fca666552254559110d",
"60c24c8ec01a8596ba5c8b85",
"60bc18bb8b971280ef13060c",
"60f83b167c76803d88b92d53",
"5bebd4111296920001d55c5a",
"60fe4c46e72a8b28dc55d376",
"5ddc07391e42a9000b2622be",
"565a4547c51d43000587507d",
"61094c7cb8c79b6a734c2d0c",
"5a5479b4ac56240001537ffa",
"6108b317855b3eb7cd588352",
"6109ab59c73e95d7a1f004a5",
"6105ac9411551a0880809277",
"5e169361afb8b0c69c239371",
"600dd1ea271cf06201979123",
"601e1253bbecc3279e4fb472")
  
pct_data <- dir_ls(here("data", "raw", "pct"), regexp = "\\.csv$") %>%
  map_dfr(read_csv, .id = "source", 
          col_types = cols(.default = "c")) %>%
  filter(stim %in% stim_list) %>% 
  filter(participant %in% participants_done) %>% 
  filter(!is.na(key_resp.keys)) %>%
  rename(resp = key_resp.keys) %>% 
  mutate(resp = case_when(
    resp == "1" ~ "fun_eng",
    resp == "2" ~ "fought_eng",
    resp == "3" ~ "feel_eng",
    resp == "4" ~ "fool_eng",
    resp == "5" ~ "son_span",
    resp == "6" ~ "su_span",
    resp == "7" ~ "fin_span")) %>% 
  mutate(frame = case_when(
    stim == "stim/f_schwa_f.wav" ~ "fricative",
    stim == "stim/p_schwa_f.wav" ~ "bilabial",
    stim == "stim/fof_f.wav" ~ "fricative",
    stim == "stim/pof_f.wav" ~ "bilabial",
    stim == "stim/feuf_f.wav" ~ "fricative",
    stim == "stim/peuf_f.wav" ~ "bilabial",
    stim == "stim/fif_f.wav" ~ "fricative",
    stim == "stim/pif_f.wav" ~ "bilabial")) %>% 
  mutate(language = "french") %>%
  mutate(phoneme = case_when(
    stim == "stim/f_schwa_f.wav" ~ "schwa",
    stim == "stim/p_schwa_f.wav" ~ "schwa",
    stim == "stim/fof_f.wav" ~ "o",
    stim == "stim/pof_f.wav" ~ "o",
    stim == "stim/fif_f.wav" ~ "i",
    stim == "stim/pif_f.wav" ~ "i",
    stim == "stim/peuf_f.wav" ~ "y",
    stim == "stim/feuf_f.wav" ~ "y")) %>% 
  select(participant, stim, resp, language, slider_2.response,
         phoneme, frame) 


pct_data$slider_2.response = as.numeric(pct_data$slider_2.response)

resp = pct_data %>% 
  group_by(stim, resp) %>% 
  summarise("response" = n(), rating = mean(slider_2.response),
            rating_sd = sd(slider_2.response)) %>% 
  separate(resp, into = c("resp", "language"), sep = "_") %>% 
  mutate(phoneme = case_when(
    stim == "stim/f_schwa_f.wav" ~ "schwa",
    stim == "stim/p_schwa_f.wav" ~ "schwa",
    stim == "stim/fof_f.wav" ~ "o",
    stim == "stim/pof_f.wav" ~ "o",
    stim == "stim/fif_f.wav" ~ "i",
    stim == "stim/pif_f.wav" ~ "i",
    stim == "stim/peuf_f.wav" ~ "y",
    stim == "stim/feuf_f.wav" ~ "y")) %>% 
  mutate(frame = case_when(
    stim == "stim/f_schwa_f.wav" ~ "fricative",
    stim == "stim/p_schwa_f.wav" ~ "bilabial",
    stim == "stim/fof_f.wav" ~ "fricative",
    stim == "stim/pof_f.wav" ~ "bilabial",
    stim == "stim/feuf_f.wav" ~ "fricative",
    stim == "stim/peuf_f.wav" ~ "bilabial",
    stim == "stim/fif_f.wav" ~ "fricative",
    stim == "stim/pif_f.wav" ~ "bilabial")) 

pct_data %>% 
  write.csv(here("scripts", "final_data_collection_pct", 
                 "data", "tidy",
                 "pct_tidy_french.csv"))

resp %>%   
  write.csv(here("scripts", "final_data_collection_pct", 
                          "data", "tidy",
                          "resp_df.fren.csv"))
