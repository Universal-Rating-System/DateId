import datetime

import pytest
import time_machine
from conftest import test_set_01
from conftest import test_set_02
from conftest import test_set_03
from conftest import test_set_leap_years

from dateid import DateId


class TestDateId:
    # @pytest.mark.parametrize("base, today, day_id, month_id", test_set_01)
    # def test_def_base_eq_today(self, base, today, day_id, month_id):
    #     with time_machine.travel(datetime.date(today[0], today[1], today[2])):
    #         base_date = datetime.date(base[0], base[1], base[2])
    #         base_date_str = datetime.date(base[0], base[1], base[2]).strftime("%Y%m%d")
    #         today_date = datetime.date.today()
    #         today_date_str = datetime.date(today[0], today[1], today[2]).strftime("%Y%m%d")
    #         date_id = DateId()
    #         assert date_id.base_date == base_date
    #         assert date_id.base_date_str == base_date_str
    #         assert date_id.target_date == today_date
    #         assert date_id.target_date_str == today_date_str
    #         assert date_id.month_id == month_id
    #         assert date_id.day_id.days == day_id
    #     pass

    @pytest.mark.parametrize("base, today, day_id, month_id", test_set_01)
    def test_def_base_eq_today(self, base, today, day_id, month_id):
        # Create the datetime instance for travel; here using midnight.
        travel_dt = datetime.datetime(today[0], today[1], today[2])

        @time_machine.travel(travel_dt)
        def run_test():
            base_date = datetime.date(*base)
            base_date_str = base_date.strftime("%Y%m%d")
            today_date = datetime.date.today()
            today_date_str = today_date.strftime("%Y%m%d")
            date_id = DateId()
            assert date_id.base_date == base_date
            assert date_id.base_date_str == base_date_str
            assert date_id.target_date == today_date
            assert date_id.target_date_str == today_date_str
            assert date_id.month_id == month_id
            assert date_id.day_id.days == day_id

        # Execute the decorated inner test.
        run_test()

    @pytest.mark.parametrize("base, today, day_id, month_id", test_set_01)
    def test_set_base_eq_today(self, base, today, day_id, month_id):
        with time_machine.travel(datetime.date(today[0], today[1], today[2])):
            base_date = datetime.date(base[0], base[1], base[2])
            base_date_str = datetime.date(base[0], base[1], base[2]).strftime("%Y%m%d")
            today_date = datetime.date.today()
            today_date_str = datetime.date(today[0], today[1], today[2]).strftime("%Y%m%d")
            date_id = DateId(p_base_date_str=base_date_str)
            assert date_id.base_date == base_date
            assert date_id.base_date_str == base_date_str
            assert date_id.target_date == today_date
            assert date_id.target_date_str == today_date_str
            assert date_id.month_id == month_id
            assert date_id.day_id.days == day_id
        pass

    @pytest.mark.parametrize("base, target, day_id, month_id", test_set_02)
    def test_set_base_eq_target_str(self, base, target, day_id, month_id):
        base_date = datetime.date(base[0], base[1], base[2])
        base_date_str = datetime.date(base[0], base[1], base[2]).strftime("%Y%m%d")
        target_date = datetime.date(target[0], target[1], target[2])
        target_date_str = datetime.date(target[0], target[1], target[2]).strftime("%Y%m%d")
        date_id = DateId(p_base_date_str=base_date_str, p_target_date_str=target_date_str)
        assert date_id.base_date == base_date
        assert date_id.base_date_str == base_date_str
        assert date_id.target_date == target_date
        assert date_id.target_date_str == target_date_str
        assert date_id.month_id == month_id
        assert date_id.day_id.days == day_id
        pass

    @pytest.mark.parametrize("base, target, day_id, month_id", test_set_02)
    def test_set_base_eq_target_day(self, base, target, day_id, month_id):
        base_date = datetime.date(base[0], base[1], base[2])
        base_date_str = datetime.date(base[0], base[1], base[2]).strftime("%Y%m%d")
        target_date = datetime.date(target[0], target[1], target[2])
        target_date_str = datetime.date(target[0], target[1], target[2]).strftime("%Y%m%d")
        date_id = DateId(p_base_date_str=base_date_str, p_target_day=day_id)
        assert date_id.base_date == base_date
        assert date_id.base_date_str == base_date_str
        assert date_id.target_date == target_date
        assert date_id.target_date_str == target_date_str
        assert date_id.month_id == month_id
        assert date_id.day_id.days == day_id
        pass

    @pytest.mark.parametrize("base, target, day_id, month_id", test_set_03)
    def test_set_base_eq_target_day_zero(self, base, target, day_id, month_id):
        base_date = datetime.date(base[0], base[1], base[2])
        base_date_str = datetime.date(base[0], base[1], base[2]).strftime("%Y%m%d")
        target_date = datetime.date(target[0], target[1], target[2])
        target_date_str = datetime.date(target[0], target[1], target[2]).strftime("%Y%m%d")
        date_id = DateId(p_base_date_str=base_date_str, p_target_day=day_id)
        assert date_id.base_date == base_date
        assert date_id.base_date_str == base_date_str
        assert date_id.target_date == target_date
        assert date_id.target_date_str == target_date_str
        assert date_id.month_id == month_id
        assert date_id.day_id.days == day_id + 1
        pass

    @pytest.mark.parametrize("year, result", test_set_leap_years)
    def test_leap_year(self, year, result):
        date_id = DateId()
        assert date_id.is_leap_year(year) == result
        pass
