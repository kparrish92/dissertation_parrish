# manually getting formants of 4 stim instead of scripting 
library(phonTools)

stim_formants <- data.frame("segment" = c("y", "i", "o", "^",
                                          "i", "o",
                                          "i", "^", "y", "u", "u", "a"),
"f1" = c(390.33, 260.18, 502.7, 487.31, 286, 460, 268, 640, 300, 322, 326, 780),
"f2" = c(2229.12, 2492.66, 1199.22, 1636.19, 2147, 1019, 2393, 1354, 1863, 992, 1238, 1244),
"is_stim" = c(1,1,1,1,0,0,0,0,0,0,0,0),
"Language" = c("Stimulus", "Stimulus","Stimulus","Stimulus","Spanish","Spanish",
               "English","English","French","Spanish","English","English"))   
  
stim_formants %>% 
  ggplot(aes(x = f2, y = f1, label = segment, color = Language)) + 
  geom_text() + scale_y_reverse() + scale_x_reverse()

# French values from Dowd et al, 1997
# Spanish and English from Bradow, 1995x

# could ensure that duration is constant.
# add reported format value from literature -done

# Make a list of the stimuli - done 

# Why AX? to see if English disc is similar between groups - 
# best disc is expected by English mono
# second best disc by Eng L1 Span L2
# third best by Sp L1 Eng L2
# fourth best by Sp mono 

# 2 continua are to increase the robustness of the finding - 