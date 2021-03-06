import pytest
import os
from renju.game.statistic import Statistic


@pytest.fixture()
def statistic():
    statistic = Statistic()
    statistic.high_score_table["#000000"] = 3
    statistic.high_score_table["#FFFFFF"] = 2
    statistic.write_in_file()
    statistic.download_score_table()
    return statistic


def test_download_score_table(statistic):
    assert statistic.high_score_table.get("#000000") == 3
    assert statistic.high_score_table.get("#FFFFFF") == 2
    os.remove(statistic.HIGH_SCORE_FILE_NAME)


def test_update_player(statistic):
    statistic.update_player((0, 0, 0))
    assert statistic.high_score_table.get("#000000") == 4
    os.remove(statistic.HIGH_SCORE_FILE_NAME)
