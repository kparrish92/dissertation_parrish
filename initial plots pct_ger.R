# Tidy phoneme categorization task --------------------------------------------
#
# Last update: 2022-3-9
# -------------------------------------------------

# Source libs -----------------------------------------------------------------

source(here::here("scripts", "perception", "00_libs.R"))

# -----------------------------------------------------------------------------



pct_data <- dir_ls(here("scripts", "german_pilot_perception", "data"), regexp = "\\.csv$") %>%
  map_dfr(read_csv, .id = "source", col_types = cols(.default = "c")) %>% 
  filter(!is.na(date)) %>% 
  filter(!is.na(slider.response)) %>% 
  filter(!is.na(key_resp_2.keys)) %>% 
  rename(resp = key_resp_2.keys) %>% 
  mutate(resp = case_when(
    resp == "1" ~ "fun_eng",
    resp == "2" ~ "fought_eng",
    resp == "3" ~ "feel_eng",
    resp == "4" ~ "fool_eng",
    resp == "5" ~ "son_span",
    resp == "6" ~ "su_span",
    resp == "7" ~ "sin_span")) 

pct_data$slider.response = as.numeric(pct_data$slider.response)

glimpse(pct_data)

resp = pct_data %>% 
  group_by(stim, resp) %>% 
  summarise("response" = n(), rating = mean(slider.response),
            rating_sd = sd(slider.response)) %>% 
  separate(resp, into = c("resp", "language"), sep = "_") %>% 
  mutate(phoneme = case_when(
    stim == "stim/f_schwa_g.wav" ~ "schwa",
    stim == "stim/p_schwa_g.wav" ~ "schwa",
    stim == "stim/faf_g.wav" ~ "a",
    stim == "stim/paf_g.wav" ~ "a",
    stim == "stim/fof_g.wav" ~ "o",
    stim == "stim/pof_g.wav" ~ "o",
    stim == "stim/fif_g.wav" ~ "i",
    stim == "stim/piep_g.wav" ~ "i")) %>% 
  mutate(frame = case_when(
    stim == "stim/f_schwa_g.wav" ~ "fricative",
    stim == "stim/p_schwa_g.wav" ~ "bilabial",
    stim == "stim/faf_g.wav" ~ "fricative",
    stim == "stim/paf_g.wav" ~ "bilabial",
    stim == "stim/fof_g.wav" ~ "fricative",
    stim == "stim/pof_g.wav" ~ "bilabial",
    stim == "stim/fif_g.wav" ~ "fricative",
    stim == "stim/piep_g.wav" ~ "bilabial")) 


p1 = resp %>% 
  filter(phoneme == "o") %>%
  ggplot(aes(x = resp, y = response)) + 
  geom_bar(stat = "identity", aes(fill = rating)) + ylim(0, 75) +
  ggtitle("responses to /o/") + facet_wrap(~frame)

p2 = resp %>% 
  filter(phoneme == "i") %>%
  ggplot(aes(x = resp, y = response)) + 
  geom_bar(stat = "identity", aes(fill = rating)) + ylim(0, 75) +
  ggtitle("responses to /i/") + facet_wrap(~frame)

p3 = resp %>% 
  filter(phoneme == "a") %>%
  ggplot(aes(x = resp, y = response)) + 
  geom_bar(stat = "identity", aes(fill = rating)) + ylim(0, 75) +
  ggtitle("responses to /a/") + facet_wrap(~frame)

p4 = resp %>% 
  filter(phoneme == "schwa") %>%
  ggplot(aes(x = resp, y = response)) + 
  geom_bar(stat = "identity", aes(fill = rating)) + ylim(0, 75) +
  ggtitle("responses to schwa") + facet_wrap(~frame)


ggarrange(p1, p2, p3, p4, 
                      labels = c("A", "B", "C", "D"),
                      ncol = 2, nrow = 2) + 
  ggtitle("Figure 1: Word categories chosen per auditory stimlus")




pct_tidy = pct_data %>% 
  mutate(phoneme = case_when(
    stim == "stim/f_schwa_g.wav" ~ "schwa",
    stim == "stim/p_schwa_g.wav" ~ "schwa",
    stim == "stim/faf_g.wav" ~ "a",
    stim == "stim/paf_g.wav" ~ "a",
    stim == "stim/fof_g.wav" ~ "o",
    stim == "stim/pof_g.wav" ~ "o",
    stim == "stim/fif_g.wav" ~ "i",
    stim == "stim/piep_g.wav" ~ "i")) %>% 
  mutate(frame = case_when(
    stim == "stim/f_schwa_g.wav" ~ "fricative",
    stim == "stim/p_schwa_g.wav" ~ "bilabial",
    stim == "stim/faf_g.wav" ~ "fricative",
    stim == "stim/paf_g.wav" ~ "bilabial",
    stim == "stim/fof_g.wav" ~ "fricative",
    stim == "stim/pof_g.wav" ~ "bilabial",
    stim == "stim/fif_g.wav" ~ "fricative",
    stim == "stim/piep_g.wav" ~ "bilabial")) %>% 
  select(participant, resp, slider.response, frame, phoneme) %>% 
  separate(resp, into = c("resp_word", "resp_language"), sep = "_") %>% 
  mutate(resp_language_b = case_when(
    resp_language == "eng" ~ 1,
    resp_language == "span" ~ 0))
  


# resp_language ~ frame + phoneme + slider.response + (1 | resp_word) + (1 | participant)

pct_tidy = 

# nmc 
null_model = lmer(resp_language_b ~ 1 + (1 | participant), 
     data = pct_tidy)

phoneme_model = lmer(resp_language_b ~ phoneme + (1 | participant), 
                     data = pct_tidy)

frame_model = lmer(resp_language_b ~ phoneme + frame +
                       (1 | participant), 
                     data = pct_tidy)


int_model = brms::brm(resp_language_b ~ phoneme + frame + phoneme:frame +
                     (1 | participant), 
                   data = pct_tidy)


anova(null_model, phoneme_model, frame_model, int_model)

summary(int_model)

df = data.frame("est" = fixef(phoneme_model))


probability_a = plogis(df$est[1])

probability_i = plogis(df$est[1] + df$est[2])
probability_o = plogis(df$est[1] + df$est[3])
probability_schwa = plogis(df$est[1] + df$est[4])



# another option - multinomial - 
# resp_word ~ phoneme + frame 
