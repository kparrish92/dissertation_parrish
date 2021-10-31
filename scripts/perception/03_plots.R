# Analyze phoneme categorization task  ---------------------------------
#
# Last update: 2021-10-24
# Analyze from pilot phoneme cat task
# - participants heard 5x of 4 vowels
# - they chose which English or Spanish vowel was the closest fit
# - they rate there choice 
# -----------------------------------------------------------------------------

# Source libs -----------------------------------------------------------------

source(here::here("scripts", "perception", "00_libs.R"))

# -----------------------------------------------------------------------------


pct <- read.csv(here("data", "tidy", "pct", "pct_tidy.csv")) %>% 
  filter(!is.na(key_resp_4.keys)) %>% 
  select(stim, participant, key_resp_4.keys, slider.response) %>% 
  rename(resp = key_resp_4.keys) %>% 
  mutate(resp = case_when(
    resp == "q" ~ "english_seek",
    resp == "y" ~ "english_sock",
    resp == "p" ~ "english_such",
    resp == "g" ~ "english_soon",
    resp == "z" ~ "spanish_sin",
    resp == "m" ~ "spanish_son",
    resp == "v" ~ "spanish_su")) %>% 
  mutate("lang" = resp) %>% 
  separate(lang, into = c("language", "word"), sep = "_") %>% 
  mutate(eng = case_when(language == "english" ~ 1,
                         language == "spanish" ~ 0))
  
# what were the popular choices per stimulus? 

desc_df <- pct %>% 
  group_by(stim, resp) %>% 
  summarise("response" = n(), rating = mean(slider.response),
            rating_sd = sd(slider.response)) %>% 
  separate(resp, into = c("language", "resp"), sep = "_")

# sys = french close front rounded vowel
# sus = french close back vowel
# sis = french close front unrounded vowel
# sos = french close-mid back vowel

# Both language condition /i/ 

# box plot of ratings
pct %>% 
  filter(stim == "stim/sis.wav") %>% 
  ggplot(aes(x = slider.response, y = resp)) + geom_boxplot() +
  ggtitle("/i/ repsonses")

# desc df for table
desc_df %>% 
  filter(stim == "stim/sis.wav") 

# bar plot 
p1 <- desc_df %>% 
  filter(stim == "stim/sis.wav") %>%
  ggplot(aes(x = resp, y = response)) + 
  geom_bar(stat = "identity", aes(fill = rating)) + ylim(0, 200) +
  ggtitle("responses to /i/")



# Spanish condition /o/
pct %>% 
  filter(stim == "stim/sos.wav") %>% 
  ggplot(aes(x = slider.response, y = resp)) + geom_boxplot() +
  ggtitle("/o/ repsonses")

desc_df %>% 
  filter(stim == "stim/sos.wav") 

# bar plot 
p2 <- desc_df %>% 
  filter(stim == "stim/sos.wav") %>%
  ggplot(aes(x = resp, y = response)) + 
  geom_bar(stat = "identity", aes(fill = rating)) + ylim(0, 200) +
  ggtitle("responses to /o/")

# Neither language /y/
pct %>% 
  filter(stim == "stim/sys.wav") %>% 
  ggplot(aes(x = slider.response, y = resp)) + geom_boxplot() +
  ggtitle("/y/ repsonses")

desc_df %>% 
  filter(stim == "stim/sys.wav") 

p3 <- desc_df %>% 
  filter(stim == "stim/sys.wav") %>%
  ggplot(aes(x = resp, y = response)) + 
  geom_bar(stat = "identity", aes(fill = rating)) + ylim(0, 200) +
  ggtitle("responses to /y/")

# English condition /^/

pct %>% 
  filter(stim == "stim/sus.wav") %>% 
  ggplot(aes(x = slider.response, y = resp)) + geom_boxplot() +
  ggtitle("/y/ repsonses")

desc_df %>% 
  filter(stim == "stim/sus.wav")

p4 <- desc_df %>% 
  filter(stim == "stim/sus.wav") %>% 
  ggplot(aes(x = resp, y = response)) + 
  geom_bar(stat = "identity", aes(fill = rating)) + ylim(0, 200) +
  ggtitle("responses to /^/")

# did the same participants stick to one language?

eng_percent <- pct %>% 
  group_by(participant) %>% 
  summarise(pct_eng = sum(eng)/20) %>% 
  mutate(pct_eng = pct_eng*100)

# plot - looks like there is variation 
eng_plot <- eng_percent %>% 
  ggplot(aes(x = pct_eng, y = reorder(participant, +pct_eng))) + 
  geom_bar(stat = "identity", aes(fill = pct_eng)) +
  theme(axis.text.y=element_blank()) +
  geom_vline(xintercept = 50, linetype = "dashed") + xlim(0, 100) +
  ylab("Participants") + xlab("Percentage English category") + 
  ggsave(here("docs", "abstracts", "new_sounds", 
              "figs", "eng_percent.png"), dpi = 1200)


pct_plot <- ggarrange(p1, p2, p3, p4, 
          labels = c("A", "B", "C", "D"),
          ncol = 2, nrow = 2) + 
  ggtitle("Figure 1: Word categories chosen per auditory stimlus") +
  ggsave(here("docs", "abstracts", "new_sounds", 
              "figs", "pct_results.png"), dpi = 1200)

ggarrange(pct_plot, eng_plot, ncol = 1) +
  ggsave(here("docs", "abstracts", "new_sounds", 
              "figs", "comb_results.png"), dpi = 1200)

# plot to check individual responses 

pct %>%  
  ggplot(aes(x = word, y = stim)) + geom_jitter()

pct %>% 
  filter(stim == "stim/sis.wav") %>% 
  filter(participant == "noid6") %>% 
  ggplot(aes(x = word, y = stim)) + 
  geom_bar(stat = "identity") + ylim(0, 200) +
  ggtitle("responses to /^/")


pct %>% 
  filter(stim == "stim/sis.wav") %>% 
  filter(participant == "noid6") %>% 
  ggplot(aes(x = word, fill = slider.response)) + 
  geom_bar() + ylim(0, 5) +
  ggtitle("responses to /^/")


pct %>% 
  filter(participant == "noid6") %>% 
  ggplot(aes(x = word, fill = mean(slider.response))) + 
  geom_bar() + ylim(0, 20) +
  ggtitle("responses to /^/")

pct %>% 
  group_by(participant, stim) %>% 
  summarise(response = sum())


#### Plot raw data ####


pct <- pct %>% 
  mutate("Auditory_Stimulus" = case_when(
    stim == "stim/sis.wav" ~ "Spanish /i/",
    stim == "stim/sos.wav" ~ "Spanish /o/",
    stim == "stim/sys.wav" ~ "French /y/",
    stim == "stim/sus.wav" ~ "English wedge"))

pct %>% 
  ggplot(aes(
    x = Auditory_Stimulus,
    y = resp
  )) +
  geom_point(
    aes(
      x = Auditory_Stimulus,
      y = resp,
      fill = slider.response
    ),
    position = position_jitterdodge(
      jitter.width = .1,
      jitter.height = 0.16,
      dodge.width = .01
    ),
    size = 2,
    alpha = .2,
    color = "steelblue",
    shape = 20,
    inherit.aes = FALSE
  ) + guides(fill=FALSE)


# facet per participant 

pct %>% 
  ggplot(aes(
    x = Auditory_Stimulus,
    y = resp
  )) +
  geom_point(
    aes(
      x = Auditory_Stimulus,
      y = resp,
      fill = slider.response
    ),
    position = position_jitterdodge(
      jitter.width = .1,
      jitter.height = 0.16,
      dodge.width = .01
    ),
    size = 2,
    alpha = .2,
    shape = 20,
    inherit.aes = FALSE
  ) +
  facet_wrap(~participant) + guides(fill=FALSE)

