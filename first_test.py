# import re
# from playwright.sync_api import Page, expect

# def test_has_title(page: Page):
#     page.goto("https://playwright.dev/")

#     # Expect a title "to contain" a substring.
#     expect(page).to_have_title(re.compile("Playwright"))

# def test_get_started_link(page: Page):
#     page.goto("https://playwright.dev/")

#     # Click the get started link.
#     page.get_by_role("link", name="Get started").click()

#     # Expects page to have a heading with the name of Installation.
#     expect(page.get_by_role("heading", name="Installation")).to_be_visible()

# import dataclasses
# @dataclasses.dataclass
# class NavbarMenuOptions:
#     SERVICES: str = 'Services'
#     PORTFOLIO: str = 'Portfolio'
#     TEAM: str = 'Team'
#     RESOURCES: str = 'Resources'
#     CAREERS: str = 'Careers'
#     BLOG: str = 'Blog'
#     CONTACT: str = 'Contact'

#     def get_all_texts(self):
#         print(dataclasses.astuple(self))
#         return dataclasses.astuple(self)
    
# s = NavbarMenuOptions().get_all_texts()
# print(list(s))

from playwright.sync_api import sync_playwright

from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     context = p.request.new_context()
#     response = context.get("https://reqres.in/api/users?page=2")
#     print(response.body())
#     assert response.ok
#     assert response.status == 200
    # assert response.headers["content-type"] == "application/json; charset=utf-8"
    # assert response.json()["name"] == "foobar"

with sync_playwright() as s:
    context = s.request.new_context()
    # https://reqres.in/api/users
    payload = {
    "name": "morpheus",
    "job": "leader"
}
    response = context.post("https://reqres.in/api/users",params=payload)
    print(response.json())