

spanish_i = data.frame(f1 = rnorm(n = 100, mean = 286, sd = 6),
                        f2 = rnorm(n = 100, 2147, 137),
                       segment = "i",
                       language = "spanish")

spanish_o = data.frame(f1 = rnorm(n = 100, mean = 460, sd = 19),
                       f2 = rnorm(n = 100, 1019, 99),
                       segment = "o",
                       language = "spanish")

english_i = data.frame(f1 = rnorm(n = 100, mean = 268, sd = 20),
                       f2 = rnorm(n = 100, 2393, 239),
                       segment = "i",
                       language = "english")

english_wedge = data.frame(f1 = rnorm(n = 100, mean = 640, sd = 39),
                       f2 = rnorm(n = 100, 1354, 134),
                       segment = "wedge",
                       language = "english")


french_i = data.frame(f1 = rnorm(n = 100, mean = 273, sd = 25),
                           f2 = rnorm(n = 100, 2524, 271),
                           segment = "i",
                           language = "french")

french_y = data.frame(f1 = rnorm(n = 100, mean = 273, sd = 25),
                      f2 = rnorm(n = 100, 2037, 125),
                      segment = "y",
                      language = "french")


french_o = data.frame(f1 = rnorm(n = 100, mean = 417, sd = 36),
                      f2 = rnorm(n = 100, 791, 80),
                      segment = "o",
                      language = "french")


french_wedge = data.frame(f1 = rnorm(n = 100, mean = 577, sd = 80),
                      f2 = rnorm(n = 100, 1063, 89),
                      segment = "wedge",
                      language = "french")

# ref for french DOI: 10.1051/shsconf/20162709003


german_y = data.frame(f1 = rnorm(n = 100, mean = 290, sd = 25),
                          f2 = rnorm(n = 100, 1700, 125),
                          segment = "y",
                          language = "german")


german_i = data.frame(f1 = rnorm(n = 100, mean = 290, sd = 25),
                      f2 = rnorm(n = 100, 2300, 271),
                      segment = "i",
                      language = "german")


german_o = data.frame(f1 = rnorm(n = 100, mean = 390, sd = 36),
                      f2 = rnorm(n = 100, 890, 80),
                      segment = "o",
                      language = "german")

german_wedge = data.frame(f1 = rnorm(n = 100, mean = 440, sd = 36),
                      f2 = rnorm(n = 100, 1740, 80),
                      segment = "wedge",
                      language = "german")

all_vowels <- rbind(english_i, english_wedge, 
      french_i, french_o, french_wedge, french_y, 
      german_o, german_wedge, german_y, german_i, 
      spanish_i, spanish_o)









## should make these points, and add a 
## mean point as geom text to the middle of each

desc_vowels <- all_vowels %>% 
  group_by(language, segment) %>% 
  summarise(mean_f1 = mean(f1), mean_f2 = mean(f2),
            sd_f1 = sd(f1), sd_f2 = sd(f2))
  

ggplot(data = all_vowels, aes(x = f2, y = f1, color = language)) + 
  geom_point(alpha = .5) + 
  scale_y_reverse() + 
  scale_x_reverse() +
  theme(legend.position = "none") +
  dark_theme_gray() +
  theme(panel.background = element_rect(fill = "#333333"),
        plot.background = element_rect(fill = "#333333", 
                                       color = "#333333"),
        panel.grid.major = element_line(color = "#5b5b5b"),
        panel.grid.minor = element_line(color = "#5b5b5b"),
        legend.background = element_rect(fill = "#333333", 
                                         color = "white"),
        legend.key = element_rect(fill = "#333333")) +
  annotate("text", x=desc_vowels$mean_f2[1], 
           y=desc_vowels$mean_f1[1], label= "i") +
  annotate("text", x=desc_vowels$mean_f2[2], 
           y=desc_vowels$mean_f1[2], label= "wedge") +
  annotate("text", x=desc_vowels$mean_f2[3], 
           y=desc_vowels$mean_f1[3], label= "i") +
  annotate("text", x=desc_vowels$mean_f2[4], 
           y=desc_vowels$mean_f1[4], label= "o") +
  annotate("text", x=desc_vowels$mean_f2[5], 
           y=desc_vowels$mean_f1[5], label= "wedge") +
  annotate("text", x=desc_vowels$mean_f2[6], 
           y=desc_vowels$mean_f1[6], label= "y") +
  annotate("text", x=desc_vowels$mean_f2[7], 
           y=desc_vowels$mean_f1[7], label= "i") +
  annotate("text", x=desc_vowels$mean_f2[8], 
           y=desc_vowels$mean_f1[8], label= "o") +
  annotate("text", x=desc_vowels$mean_f2[9], 
           y=desc_vowels$mean_f1[9], label= "wedge") +
  annotate("text", x=desc_vowels$mean_f2[10], 
           y=desc_vowels$mean_f1[10], label= "y") +
  annotate("text", x=desc_vowels$mean_f2[11], 
           y=desc_vowels$mean_f1[11], label= "i") +
  annotate("text", x=desc_vowels$mean_f2[12], 
           y=desc_vowels$mean_f1[12], label= "o") +
  ggsave(here("slides", "img", "vowels.png"))


