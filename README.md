# Task 1: Software configuration
## Subtask 1: Why did I choose to participate in the challenge portfolio?

Nowadays, IT is a very popular sphere, so nothing strange that I am interested QA as a first step in it. I am working for now, but my work is not interested for me anymore because I don't feel that I can develop myself there. Another and not less important reason is the salary which is Ukrainian and not enough for living abroad, so I decided that it's my chance for a new life. I hope it will be interesting for me but if not - I want to continue self-development in the IT, but maybe in Project Managment, where I should contact with people (It makes me a lot of pleasure).

Sorry for my open-hearted text, but every word is **truth**.

# Task 2: Selectors
## All the elements that are on the login page:

| Elements                     | 1 Selector                                     | 2 Selector                                            | 3 Selector                                                   |
|------------------------------|------------------------------------------------|-------------------------------------------------------|--------------------------------------------------------------|
| *title_form*                 | `//*[@id="__next"]/form/div/div[1]/h5`         | `//*[text()="Scouts Panel"]`                          | `//child::div/h5`                                            |
| *login_form*                 | `//*[@id="login"]`                             | `//input[@name="login"]`                              | `input[type="text"]`                                         | 
| *password_form*              | `//*[@id="password"]`                          | `//*[text()="Password" or text()="Hasło"]`            | `input[type="password"]`                                     |
| *remind_password_hyperlink*  | `//*[@id="__next"]/form/div/div[1]/a`          | `//a[contains(@class, "MuiTypography-colorPrimary")]` | `//a[text()="Remind password" or text()="Przypomnij hasło"]` |
| *language_select*            | `//*[@id="__next"]/form/div/div[2]/div/input`  | `//input[@value="en" or @value="pl"]`                 | `//input[@class="MuiSelect-nativeInput"]`                    |
| *sign_in_button*             | `//*[@id="__next"]/form/div/div[2]/button`     | `//*[contains(@type, "submit")]`                      | `//child::div/button`                                        | 