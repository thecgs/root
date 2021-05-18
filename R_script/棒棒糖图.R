library(ggpubr)
library(ggplot2)
setwd("C:/Users/22954/Desktop")
data = read.table("所有免疫细胞相关性.txt",header=T,sep="\t",check.names=F)
data =na.omit(data)
data$Group <- as.factor(data$Group)

ggdotchart(data,y='Correlation',x='Immune_cells_infiltrates',sorting='descending',add='segments',rotate=TRUE,group='Group',ggtheme = theme_pubr(),add.params = list(color = "lightgray", size = 0.5)) +theme(axis.text.y  = element_text(size=5),text = element_text(size=6)) + geom_point(color='black',size=3,,show.legend =T) +geom_point(aes(color=Group),size=2,show.legend =T) + theme(legend.position = 'right')


ggdotchart(data,y='Correlation',x='Immune_cells_infiltrates',sorting='descending',add='segments',rotate=TRUE,group='Group',ggtheme = theme_pubr()) + theme(axis.text.y  = element_text(size=5),text = element_text(size=6),legend.position = 'right') + geom_point(aes(color=Group,size=-log(adj.p)),show.legend =T) + scale_size_continuous(range = c(2,7))