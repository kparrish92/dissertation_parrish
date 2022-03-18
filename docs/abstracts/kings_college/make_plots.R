
library(ggpubr)

report_df_e = read.csv(here("scripts", "final_data_collection_pct", 
                          "data", "tidy",
                          "report_bilabial_eng_l1.csv"))


report_df_s = read.csv(here("scripts", "spanish_bilingual_pct", 
                            "data", "tidy",
                            "report_bilabial_span_l1.csv"))



e = report_df_e %>% 
  ggplot(aes(x = estimate, y = phoneme, color = language,
             xmin=hdi_hi, xmax=hdi_lo)) + 
  geom_pointrange(position = position_dodge(width = .5), 
                  shape = 21, fill = "white") + 
  xlim(.45,.75) + 
  geom_vline(xintercept = .5, linetype = "dashed") +
  scale_color_manual(values=c("#1F9646", "darkgoldenrod3"))  + 
  xlab("Probability") + ylab("Phoneme of stimulus") +
  theme_bw() +
  theme(panel.background = element_rect(fill = "grey79"),
        legend.position = "bottom") + 
  theme(legend.position = "bottom") + 
  ggtitle("English L1")


s = report_df_s %>% 
  ggplot(aes(x = estimate, y = phoneme, color = language,
             xmin=hdi_hi, xmax=hdi_lo)) + 
  geom_pointrange(position = position_dodge(width = .5), 
                  shape = 21, fill = "white") + 
  xlim(.45,.75) + 
  geom_vline(xintercept = .5, linetype = "dashed") +
  scale_color_manual(values=c("#1F9646", "darkgoldenrod3"))  + 
  xlab("Probability") + ylab("Phoneme of stimulus") +
  theme_bw() +
  theme(panel.background = element_rect(fill = "grey79"),
        legend.position = "bottom") + 
  theme(legend.position = "bottom") + 
  ggtitle("Spanish L1")


ggarrange(e, s) + ggsave(here("docs", "abstracts", "kings_college", 
                              "figs", "prob_plots.png"), dpi = 300)
