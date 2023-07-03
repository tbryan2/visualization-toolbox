

# Load the library
library(ggplot2)

# Create the scatter plot
ggplot(df, aes(x = yards_gained, y = next_season_yards)) +
    geom_point() +
    labs(
        x = "Yards Gained in Current Season",
        y = "Yards Gained in Next Season",
        title = "Comparison of Yards Gained in Consecutive Seasons"
    ) +
    theme_minimal()
