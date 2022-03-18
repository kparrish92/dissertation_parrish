

source(here::here("scripts", "perception", "00_libs.R"))


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






library(lmerTest)
null = lme4::lmer(eng ~ 1 + (1 | participant),
                  data = pct)
mod = lme4::lmer(eng ~ stim + (1 | participant),
         data = pct)

mod2 = lme4::lmer(eng ~ stim + slider.response + (1 | participant),
                 data = pct)

mod3 = lme4::lmer(eng ~ stim + slider.response + 
                    stim:slider.response + (1 | participant),
                  data = pct)

anova(null, mod, mod2, mod3)

summary(mod3)

# do adjustments before plogis 

fixef_mod = as.data.frame(fixef(mod))

# these are the probabilites that 
# an English category will be chosen

prob_i = plogis(fixef_mod$`fixef(mod)`[1])
prob_o = plogis(fixef_mod$`fixef(mod)`[1] + fixef_mod$`fixef(mod)`[2])
prob_schwa = plogis(fixef_mod$`fixef(mod)`[1] + fixef_mod$`fixef(mod)`[3])   
prob_y = plogis(fixef_mod$`fixef(mod)`[1] + fixef_mod$`fixef(mod)`[4])

plogis(.36)
summary(df)

mod2 = lmer(slider.response ~ resp + (1 | participant), 
            data = pct)

summary(mod2)



# response percent ~ language + 
# stimulus vowel + answer vowel + consonant context