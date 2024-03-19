# TSP-24
Tracking Student Progress and Identification of Students at Risks

[Our landing page](https://sites.google.com/view/techlaunchertsp/) <br>
[Our google drive repo](https://drive.google.com/drive/folders/1IwTgMJIzD3xh9bObPsscaXqt6ISCbY_c?hl=en_GB) <br>
[Our team management tool](https://id.atlassian.com/invite/p/jira-software?id=lpVVj6RHTMe3sESiFFil5A) <br>


# Git Development Strategy

## Main Branches

Our `main` branch is our production branch

Our `develop` branch is for merging our development code but is not released for production

We follow a feature driven development (FDD) approach, this is followed in git with our branching strategies

## Branching
When developing a feature, or a code related task, we branch off of our `develop` branch. The naming convention follows the Jira user story or task being worked on. Reason why is because we are able to track development activity like this on Jira tasks

Such as if a task called "KAN-80" titled "Git Branching Strategy", the branch would be called `KAN-80-git-branching-strategy`.

## Commits

Commits follow the same naming convention: prefix with the Jira task name "KAN-80 \<message\>"

## Pull Requests

Pull requests are how we review code, once development is ready, we submit a pull request, following the same naming convention as above. 

