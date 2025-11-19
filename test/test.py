from component.search import Scrapper


def test_run_scrapper_links_exist(capsys):
    scrapper = Scrapper()
    dork = ["google"]
    scrapper.run_scrapper(dork)
    result = capsys.readouterr()
    assert "https://" in result.out
