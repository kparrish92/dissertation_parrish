eng = read.csv(here("scripts", "final_data_collection_pct", 
               "data", "tidy", "all_pct.tidy,csv")) %>% 
  mutate(l1 = "english")

span = read.csv(here("scripts", "spanish_bilingual_pct", 
                        "data", "tidy", "all_pct.tidy_sp.csv")) %>% 
  mutate(l1 = "spanish")

all = rbind(eng, span)

mod_tost = brm(language_num ~ l1*stim_language + (1 | participant), data = all)

fixef(mod_tost)


mcmc_areas(mod_tost,
           pars = c("b_l1spanish",
                    "b_stim_languageGerman",
                    "b_l1spanish:stim_languageGerman"),
           prob = 0.8) 


library(bayestestR)
library(see)

rope(mod_tost)

x = rope(mod_tost, range = c(-0.18, 0.18))
plot(x, dpi = 300)

rope_range(mod_tost)
