## Issue No.1: Multiple SSH Keys on the Same Device

**State**: ==Solved==

It's very common to have multiple GitHub or GitLab accounts and work on one local machine to interact with the remote repositories.

At the very beginning, I only work on one GitLab account, but now I have another account from Duke University. I also need to work with my GitHub account to build some other projects. So it's about time to understand the concepts and how SSH, git, and repositories work together.

Here are useful resources:

- This Stack Overflow [question](https://stackoverflow.com/questions/67651140/multiple-github-username-and-email-on-same-device) provides a throughout and in-depth discussion on how Git and SSH work, and how to manage multiple SSH keys and set up different Git configurations for different repos.
- In this Stack Overflow [question](https://stackoverflow.com/questions/4220416/can-i-specify-multiple-users-for-myself-in-gitconfig), there are several answers on how to set different Git configurations. includeIf (conditional includes) is the official solution introduced in Git 2.13.
- For a long time, my repo didn't recognize me as the legal user to git push. The error message is something like "GitHub remote permission denied...". This Stack Overflow [question](https://stackoverflow.com/questions/47465644/github-remote-permission-denied) talks about the reason and solution, which refers to this GitHub official [article](https://docs.github.com/en/get-started/getting-started-with-git/updating-credentials-from-the-macos-keychain).

## 