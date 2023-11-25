'''Creat integer for a date

Calculate an integer value for months and dates from a base date
'''
import datetime
import logging
import sys
from pathlib import Path

import beetools

_VERSION = '1.3.1'
_path = Path(sys.argv[0])
_name = _path.stem


class DateId:
    '''Calculate an integer value for months and dates from a base date'''

    def __init__(self, p_parent_log_name, p_base_date_str='2008/01/01', p_target_date_str='', p_target_day=''):
        '''Calculate an integer value for months and dates from a base date'''
        self.log_name = f'{p_parent_log_name}.{_name}'
        self.logger = logging.getLogger(self.log_name)
        self.logger.info('Start')
        self.version = _VERSION
        self.success = False
        self.base_date_str = p_base_date_str
        self.base_date_str = self.base_date_str.replace('-', '')
        self.base_date_str = self.base_date_str.replace('/', '')
        self.base_date = datetime.date(
            int(self.base_date_str[:4]), int(self.base_date_str[4:6]), int(self.base_date_str[-2:])
        )
        self.day_id = 0
        self.target_date = None
        self.target_date_str = None
        if p_target_date_str:
            self.calc_day_id(p_target_date_str=p_target_date_str)
            self.calc_month_id(p_target_date_str=p_target_date_str)
        elif p_target_day:
            self.calc_day_id(p_target_day=p_target_day)
            self.calc_month_id(p_target_day=p_target_day)
        else:
            p_target_date_str = datetime.datetime.now().strftime('%Y-%m-%d')
            self.calc_day_id(p_target_date_str=p_target_date_str)
            self.calc_month_id(p_target_date_str=p_target_date_str)

    # end __init__

    def calc_day_id(self, p_target_date_str='', p_target_day=''):
        '''Returns the date id of the target date'''
        if p_target_date_str:
            self.target_date_str = p_target_date_str.replace('-', '')
            self.target_date_str = self.target_date_str.replace('/', '')
            self.target_date = datetime.date(
                int(self.target_date_str[:4]), int(self.target_date_str[4:6]), int(self.target_date_str[-2:])
            )
        elif p_target_day:
            self.specific_date(p_target_day)
        one_day = datetime.timedelta(days=1)
        self.day_id = self.target_date - self.base_date + one_day
        return self.day_id.days

    # end calc_day_id

    def generate_range(self, p_start_date_parm, p_end_date_parm):
        '''Returns a range of date_id's in Tuple structure'''
        one_day = datetime.timedelta(days=1)
        if isinstance(p_start_date_parm, str):
            start_date_parm = p_start_date_parm.replace('-', '')
            start_date_parm = start_date_parm.replace('/', '')
            start_date = datetime.date(int(start_date_parm[:4]), int(start_date_parm[4:6]), int(start_date_parm[-2:]))
        elif isinstance(p_start_date_parm, int):
            start_date_day = datetime.timedelta(days=p_start_date_parm)
            start_date = self.base_date + start_date_day - one_day
        if isinstance(p_end_date_parm, str):
            end_date_parm = p_end_date_parm.replace('-', '')
            end_date_parm = end_date_parm.replace('/', '')
            end_date = datetime.date(int(end_date_parm[:4]), int(end_date_parm[4:6]), int(end_date_parm[-2:]))
        elif isinstance(p_end_date_parm, int):
            end_date_day = datetime.timedelta(days=p_end_date_parm)
            end_date = self.base_date + end_date_day - one_day
        i_len = end_date - start_date
        process_date = start_date
        days_tbl = []
        months_tbl = []
        old_month_id = self.calc_month_id(process_date.strftime('%Y-%m-%d')) - 1
        for i in range(i_len.days + 1):
            month_id = self.calc_month_id(process_date.strftime('%Y-%m') + '-01')
            day_id = self.calc_day_id(process_date.strftime('%Y-%m-%d'))
            row_days = (day_id, month_id, process_date.year, process_date.month, process_date.day, process_date)
            days_tbl.append(row_days)
            if month_id != old_month_id:
                row_months = (
                    month_id,
                    process_date.year,
                    process_date.month,
                    self.calc_day_id(process_date.strftime('%Y-%m') + '-01'),
                )
                months_tbl.append(row_months)
            process_date += one_day
            old_month_id = month_id
        return days_tbl, months_tbl

    # end generate_range

    def is_leap_year(self, p_target_year):
        '''Determines if year is a leap year'''
        if p_target_year % 4 != 0:
            success = False
        elif p_target_year % 100 != 0:
            success = True
        elif p_target_year % 400 == 0:
            success = False
        else:
            success = True
        return success

    # end is_leap_year

    def calc_month_id(self, p_target_date_str='', p_target_day=''):
        '''Returns the month id of the target date'''
        if p_target_date_str:
            self.target_date_str = p_target_date_str.replace('-', '')
            self.target_date_str = self.target_date_str.replace('/', '')
            self.target_date = datetime.date(
                int(self.target_date_str[:4]), int(self.target_date_str[4:6]), int(self.target_date_str[-2:])
            )
        elif p_target_day:
            self.specific_date(p_target_day)
        self.month_id = (self.target_date.year - self.base_date.year) * 12
        self.month_id += self.target_date.month - self.base_date.month + 1
        return self.month_id

    # end calc_month_id

    def specific_date(self, p_day_id):
        '''Returns the date in string format for the p_day_id'''
        self.day_id = datetime.timedelta(days=p_day_id)
        one_day = datetime.timedelta(days=1)
        self.target_date = self.base_date + self.day_id - one_day
        self.target_date_str = self.target_date.strftime('%Y%m%d')
        return self.target_date_str

    # end specific_date


# end DateId


def do_tests(p_app_path='', p_cls=True):
    '''Test the class methods.  Also called by the PackageIt PIP app to
    test the module during PIP installation.
    '''

    def basic_test():
        '''Definition'''

        def test_month_id(p_base_date_str, p_target_date_str):
            '''Mechanical way to calculate the month_id.  Used to test the DateId.month_id
            value.
            '''
            base_date_str = p_base_date_str.replace('-', '')
            base_date_str = base_date_str.replace('/', '')
            target_date_str = p_target_date_str.replace('-', '')
            target_date_str = target_date_str.replace('/', '')
            base_date = datetime.date(int(base_date_str[:4]), int(base_date_str[4:6]), int(base_date_str[-2:]))
            end_date = datetime.date(int(target_date_str[:4]), int(target_date_str[4:6]), int(target_date_str[-2:]))
            process_date = base_date
            one_day = datetime.timedelta(days=1)
            if end_date >= base_date:
                end = end_date - base_date + one_day
                if process_date.day != 1:
                    month_cntr = 1
                else:
                    month_cntr = 0
                for day_cntr in range(1, end.days + 1, 1):
                    if process_date.day == 1:
                        month_cntr += 1
                    if day_cntr < end.days:
                        process_date += one_day
                day_id_dict = {
                    'day_id': day_cntr,
                    'MonthId': month_cntr,
                    'SpecificYear': process_date.year,
                    'SpecificMonth': process_date.month,
                    'SpecificDay': process_date.day,
                    'SpecificDate': process_date,
                }
            else:
                end = base_date - end_date - one_day
                process_date = base_date - one_day
                month_cntr = 0
                day_cntr = 0
                for day_cntr in range(0, end.days, 1):
                    if process_date.day == 1:
                        month_cntr -= 1
                    if day_cntr < end.days:
                        process_date -= one_day
                day_id_dict = {
                    'day_id': -day_cntr - 1,
                    'MonthId': month_cntr,
                    'SpecificYear': process_date.year,
                    'SpecificMonth': process_date.month,
                    'SpecificDay': process_date.day,
                    'SpecificDate': process_date,
                }
            return day_id_dict

        # end test_month_id

        success = True
        date_id = DateId(_name)
        now_date_id = datetime.date.today() - datetime.date(2008, 1, 1)
        now_date_id += datetime.timedelta(days=1)
        success = date_id.base_date_str == '20080101' and date_id.day_id == now_date_id and success
        date_id = DateId(_name, '2008-01-01', p_target_date_str='2008-02-01')
        success = date_id.day_id.days == 32 and success
        date_id = DateId(_name, '2008-01-01', p_target_day=32)
        success = date_id.target_date_str == '20080201' and success
        success = date_id.base_date == datetime.date(2008, 1, 1) and success
        success = date_id.calc_day_id('2008-01-01') == 1 and success
        success = date_id.calc_day_id(p_target_day=1) == 1 and success
        success = date_id.calc_day_id('2008-01-02') == 2 and success
        success = date_id.calc_day_id(p_target_day=2) == 2 and success
        success = date_id.calc_day_id('2007-12-31') == 0 and success
        success = date_id.calc_day_id(p_target_day=0) == 0 and success
        success = date_id.calc_day_id('2007-12-30') == -1 and success
        success = date_id.calc_day_id(p_target_day=-1) == -1 and success
        success = not date_id.is_leap_year(2009) and success
        success = not date_id.is_leap_year(2000) and success
        success = date_id.is_leap_year(2100) and success
        success = date_id.is_leap_year(2016) and success
        target_date = '2008-01-01'
        success = (
            date_id.calc_month_id(target_date) == test_month_id(date_id.base_date_str, target_date)['MonthId']
            and success
        )
        target_date = '2008-01-31'
        success = (
            date_id.calc_month_id(target_date) == test_month_id(date_id.base_date_str, target_date)['MonthId']
            and success
        )
        target_date = '2008-02-01'
        success = (
            date_id.calc_month_id(target_date) == test_month_id(date_id.base_date_str, target_date)['MonthId']
            and success
        )
        target_date = '2008-02-15'
        success = (
            date_id.calc_month_id(target_date) == test_month_id(date_id.base_date_str, target_date)['MonthId']
            and success
        )
        target_date = '2009-02-01'
        success = (
            date_id.calc_month_id(target_date) == test_month_id(date_id.base_date_str, target_date)['MonthId']
            and success
        )
        target_date = '2007-12-31'
        success = (
            date_id.calc_month_id(target_date) == test_month_id(date_id.base_date_str, target_date)['MonthId']
            and success
        )
        target_date = '2007-12-01'
        success = (
            date_id.calc_month_id(target_date) == test_month_id(date_id.base_date_str, target_date)['MonthId']
            and success
        )
        target_date = '2007-11-30'
        success = (
            date_id.calc_month_id(target_date) == test_month_id(date_id.base_date_str, target_date)['MonthId']
            and success
        )
        target_date = '2007-11-15'
        success = (
            date_id.calc_month_id(target_date) == test_month_id(date_id.base_date_str, target_date)['MonthId']
            and success
        )
        target_date = '2006-11-30'
        success = (
            date_id.calc_month_id(target_date) == test_month_id(date_id.base_date_str, target_date)['MonthId']
            and success
        )
        test_month_tbl = [(-1, 2007, 11, -60), (0, 2007, 12, -30), (1, 2008, 1, 1), (2, 2008, 2, 32)]
        test_day_tbl = [
            (-32, -1, 2007, 11, 29, datetime.date(2007, 11, 29)),
            (-31, -1, 2007, 11, 30, datetime.date(2007, 11, 30)),
            (-30, 0, 2007, 12, 1, datetime.date(2007, 12, 1)),
            (-29, 0, 2007, 12, 2, datetime.date(2007, 12, 2)),
            (-28, 0, 2007, 12, 3, datetime.date(2007, 12, 3)),
            (-27, 0, 2007, 12, 4, datetime.date(2007, 12, 4)),
            (-26, 0, 2007, 12, 5, datetime.date(2007, 12, 5)),
            (-25, 0, 2007, 12, 6, datetime.date(2007, 12, 6)),
            (-24, 0, 2007, 12, 7, datetime.date(2007, 12, 7)),
            (-23, 0, 2007, 12, 8, datetime.date(2007, 12, 8)),
            (-22, 0, 2007, 12, 9, datetime.date(2007, 12, 9)),
            (-21, 0, 2007, 12, 10, datetime.date(2007, 12, 10)),
            (-20, 0, 2007, 12, 11, datetime.date(2007, 12, 11)),
            (-19, 0, 2007, 12, 12, datetime.date(2007, 12, 12)),
            (-18, 0, 2007, 12, 13, datetime.date(2007, 12, 13)),
            (-17, 0, 2007, 12, 14, datetime.date(2007, 12, 14)),
            (-16, 0, 2007, 12, 15, datetime.date(2007, 12, 15)),
            (-15, 0, 2007, 12, 16, datetime.date(2007, 12, 16)),
            (-14, 0, 2007, 12, 17, datetime.date(2007, 12, 17)),
            (-13, 0, 2007, 12, 18, datetime.date(2007, 12, 18)),
            (-12, 0, 2007, 12, 19, datetime.date(2007, 12, 19)),
            (-11, 0, 2007, 12, 20, datetime.date(2007, 12, 20)),
            (-10, 0, 2007, 12, 21, datetime.date(2007, 12, 21)),
            (-9, 0, 2007, 12, 22, datetime.date(2007, 12, 22)),
            (-8, 0, 2007, 12, 23, datetime.date(2007, 12, 23)),
            (-7, 0, 2007, 12, 24, datetime.date(2007, 12, 24)),
            (-6, 0, 2007, 12, 25, datetime.date(2007, 12, 25)),
            (-5, 0, 2007, 12, 26, datetime.date(2007, 12, 26)),
            (-4, 0, 2007, 12, 27, datetime.date(2007, 12, 27)),
            (-3, 0, 2007, 12, 28, datetime.date(2007, 12, 28)),
            (-2, 0, 2007, 12, 29, datetime.date(2007, 12, 29)),
            (-1, 0, 2007, 12, 30, datetime.date(2007, 12, 30)),
            (0, 0, 2007, 12, 31, datetime.date(2007, 12, 31)),
            (1, 1, 2008, 1, 1, datetime.date(2008, 1, 1)),
            (2, 1, 2008, 1, 2, datetime.date(2008, 1, 2)),
            (3, 1, 2008, 1, 3, datetime.date(2008, 1, 3)),
            (4, 1, 2008, 1, 4, datetime.date(2008, 1, 4)),
            (5, 1, 2008, 1, 5, datetime.date(2008, 1, 5)),
            (6, 1, 2008, 1, 6, datetime.date(2008, 1, 6)),
            (7, 1, 2008, 1, 7, datetime.date(2008, 1, 7)),
            (8, 1, 2008, 1, 8, datetime.date(2008, 1, 8)),
            (9, 1, 2008, 1, 9, datetime.date(2008, 1, 9)),
            (10, 1, 2008, 1, 10, datetime.date(2008, 1, 10)),
            (11, 1, 2008, 1, 11, datetime.date(2008, 1, 11)),
            (12, 1, 2008, 1, 12, datetime.date(2008, 1, 12)),
            (13, 1, 2008, 1, 13, datetime.date(2008, 1, 13)),
            (14, 1, 2008, 1, 14, datetime.date(2008, 1, 14)),
            (15, 1, 2008, 1, 15, datetime.date(2008, 1, 15)),
            (16, 1, 2008, 1, 16, datetime.date(2008, 1, 16)),
            (17, 1, 2008, 1, 17, datetime.date(2008, 1, 17)),
            (18, 1, 2008, 1, 18, datetime.date(2008, 1, 18)),
            (19, 1, 2008, 1, 19, datetime.date(2008, 1, 19)),
            (20, 1, 2008, 1, 20, datetime.date(2008, 1, 20)),
            (21, 1, 2008, 1, 21, datetime.date(2008, 1, 21)),
            (22, 1, 2008, 1, 22, datetime.date(2008, 1, 22)),
            (23, 1, 2008, 1, 23, datetime.date(2008, 1, 23)),
            (24, 1, 2008, 1, 24, datetime.date(2008, 1, 24)),
            (25, 1, 2008, 1, 25, datetime.date(2008, 1, 25)),
            (26, 1, 2008, 1, 26, datetime.date(2008, 1, 26)),
            (27, 1, 2008, 1, 27, datetime.date(2008, 1, 27)),
            (28, 1, 2008, 1, 28, datetime.date(2008, 1, 28)),
            (29, 1, 2008, 1, 29, datetime.date(2008, 1, 29)),
            (30, 1, 2008, 1, 30, datetime.date(2008, 1, 30)),
            (31, 1, 2008, 1, 31, datetime.date(2008, 1, 31)),
            (32, 2, 2008, 2, 1, datetime.date(2008, 2, 1)),
            (33, 2, 2008, 2, 2, datetime.date(2008, 2, 2)),
        ]
        start_date = '2007-11-29'
        end_date = '2008-02-02'
        (day_tbl, month_tbl) = date_id.generate_range(start_date, end_date)
        start_date = -32
        end_date = 33
        (day_tbl, month_tbl) = date_id.generate_range(start_date, end_date)
        success = beetools.is_struct_the_same(day_tbl, test_day_tbl) and success
        success = beetools.is_struct_the_same(month_tbl, test_month_tbl) and success
        success = date_id.specific_date(0) == '20071231' and success
        success = date_id.specific_date(1) == '20080101' and success
        success = date_id.specific_date(-1) == '20071230' and success
        return success

    # end basic_test

    success = True
    b_tls = beetools.Archiver(_name, _VERSION, __doc__[0], p_app_path=p_app_path, p_cls=p_cls)
    logger = logging.getLogger(_name)
    logger.setLevel(beetools.DEF_LOG_LEV)
    file_handle = logging.FileHandler(beetools.LOG_FILE_NAME, mode='w')
    file_handle.setLevel(beetools.DEF_LOG_LEV_FILE)
    console_handle = logging.StreamHandler()
    console_handle.setLevel(beetools.DEF_LOG_LEV_CON)
    file_format = logging.Formatter(beetools.LOG_FILE_FORMAT, datefmt=beetools.LOG_DATE_FORMAT)
    console_format = logging.Formatter(beetools.LOG_CONSOLE_FORMAT)
    file_handle.setFormatter(file_format)
    console_handle.setFormatter(console_format)
    logger.addHandler(file_handle)
    logger.addHandler(console_handle)

    b_tls.print_header(p_cls=p_cls)
    success = basic_test()
    beetools.result_rep(success, 'Done')
    b_tls.print_footer()
    if success:
        return b_tls.archive_path
    return False


# end do_tests

if __name__ == '__main__':
    do_tests(p_app_path=_path)
# end __main__
