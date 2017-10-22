Demonstration of a bug in the api with which you can get list forks with forks of hidden users that are not visible on Forks page and obtain information about a hidden user.

### Example of use

```
❯ python3.6 get_hidden_user_from_forks.py dimka665 vk
https://github.com/nibirunemisis
https://api.github.com/users/nibirunemisis
```

```
❯ python3.6 get_hidden_user_from_forks.py sindresorhus pure
https://github.com/lockyluchiano
https://api.github.com/users/lockyluchiano 

https://github.com/din982
https://api.github.com/users/din982 

https://github.com/grubern
https://api.github.com/users/grubern 

https://github.com/zseti
https://api.github.com/users/zseti 

https://github.com/jamiepg1
https://api.github.com/users/jamiepg1 

```