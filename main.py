import pandas as pd
import matplotlib.pyplot as plt
# Data Attribution: JHU CSSE COVID-19 Data, found at https://github.com/CSSEGISandData/COVID-19, is licensed under
# the Creative Commons Attribution 4.0 International (CC BY 4.0)

def get_daily(nums):
    daily = [0]
    for i in range(1, len(nums)):
        daily.append(nums[i] - nums[i-1])
    return daily


def get_seven_day_average(nums):
    return [sum(nums[i:i+7])/7 for i in range(len(nums)-7)]


def main():
    prefix = \
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'
    cases_csv = prefix + 'time_series_covid19_confirmed_US.csv'
    deaths_csv = prefix + 'time_series_covid19_deaths_US.csv'

    case = pd.read_csv(cases_csv).set_index("UID", drop=False)
    dead = pd.read_csv(deaths_csv).set_index("UID", drop=False)
    dates = []

    LA_total_cases = list(case.loc[84006037, '1/22/20':])
    LA_case = get_daily(LA_total_cases)
    LA_case7 = get_seven_day_average(LA_case)

    LA_total_dead = list(dead.loc[84006037, '1/22/20':])
    LA_dead = get_daily(LA_total_dead)
    LA_dead7 = get_seven_day_average(LA_dead)

    CA_total_cases = []
    state_total_cases = case.loc[84006001:84006115, '1/22/20':]
    for each in state_total_cases:
        CA_total_cases.append(sum(state_total_cases.loc[:, each]))
        dates.append(each)
    CA_case = get_daily(CA_total_cases)
    CA_case7 = get_seven_day_average(CA_case)

    CA_total_dead = []
    state_total_dead = dead.loc[84006001:84006115, '1/22/20':]
    for each in state_total_dead:
        CA_total_dead.append(sum(state_total_dead.loc[:, each]))
    CA_dead = get_daily(CA_total_dead)
    CA_dead7 = get_seven_day_average(CA_dead)

    US_total_cases = []
    country_total_cases = case.loc[:, '1/22/20':]
    for each in country_total_cases:
        US_total_cases.append(sum(country_total_cases.loc[:, each]))
    US_case = get_daily(US_total_cases)
    US_case[0] = 1
    US_case7 = get_seven_day_average(US_case)

    US_total_dead = []
    country_total_dead = dead.loc[:, '1/22/20':]
    for each in country_total_dead:
        US_total_dead.append(sum(country_total_dead.loc[:, each]))
    US_dead = get_daily(US_total_dead)
    US_dead7 = get_seven_day_average(US_dead)

    background_color = '#AAAA99'
    case_color = 'tab:blue'
    dead_color = 'mediumvioletred'
    grid_color = 'gray'
    label_size = 14
    title_size = 24

    fig, (ax1, ax3, ax5) = plt.subplots(3, sharex='all')
    fig.set_facecolor(background_color)

    lc = pd.Series(LA_case7, index=pd.date_range('1/28/2020', periods=len(LA_case7)))
    ax1.plot(lc, color=case_color)
    ax1.set_title('Los Angeles County')
    ax1.set_facecolor(background_color)
    ax1.grid(True, color=grid_color)
    ax1.set_ylabel('Cases (Seven-Day Average)', color=case_color, fontsize=label_size)
    ax2 = ax1.twinx()
    ld = pd.Series(LA_dead7, index=pd.date_range('1/28/2020', periods=len(LA_dead7)))
    ax2.plot(ld, color=dead_color)
    ax2.set_ylim([-1.5, max(LA_dead7) * 2])
    ax2.set_ylabel('Deaths (Seven-Day Average)', color=dead_color, fontsize=label_size)
    plt.legend(
        title="LA County\nCases: "+str(LA_total_cases[-1])+"\nDeaths: "+str(LA_total_dead[-1])+"\n\n"
              + dates[-1] + "\nCases: " + str(LA_case[-1]) + "\nDeaths: " + str(LA_dead[-1]), title_fontsize=title_size,
        loc='center left', bbox_to_anchor=(1.05, 0.5), facecolor=background_color, edgecolor=background_color)

    cc = pd.Series(CA_case7, index=pd.date_range('1/28/2020', periods=len(CA_case7)))
    ax3.plot(cc, color=case_color)
    ax3.set_title('California')
    ax3.set_facecolor(background_color)
    ax3.grid(True, color=grid_color)
    ax3.set_ylabel('Cases (Seven-Day Average)', color=case_color, fontsize=label_size)
    ax4 = ax3.twinx()
    cd = pd.Series(CA_dead7, index=pd.date_range('1/28/2020', periods=len(CA_dead7)))
    ax4.plot(cd, color=dead_color)
    ax4.set_ylim([-15, max(CA_dead7) * 2])
    ax4.set_ylabel('Deaths (Seven-Day Average)', color=dead_color, fontsize=label_size)
    plt.legend(
        title="California\nCases: " + str(CA_total_cases[-1]) + "\nDeaths: " + str(CA_total_dead[-1]) + "\n\n"
              + dates[-1] + "\nCases: " + str(CA_case[-1]) + "\nDeaths: " + str(CA_dead[-1]), title_fontsize=title_size,
        loc='center left', bbox_to_anchor=(1.05, 0.5), facecolor=background_color, edgecolor=background_color)

    uc = pd.Series(US_case7, index=pd.date_range('1/28/2020', periods=len(US_case7)))
    ax5.plot(uc, color=case_color)
    ax5.set_title('United States')
    ax5.set_facecolor(background_color)
    ax5.grid(True, color=grid_color)
    ax5.set_ylabel('Cases (Seven-Day Average)', color=case_color, fontsize=label_size)
    ax6 = ax5.twinx()
    ud = pd.Series(US_dead7, index=pd.date_range('1/28/2020', periods=len(US_dead7)))
    ax6.plot(ud, color=dead_color)
    ax6.set_ylim([-150, max(US_dead7) * 2])
    ax6.set_ylabel('Deaths (Seven-Day Average)', color=dead_color, fontsize=label_size)
    plt.legend(
        title="United States\nCases: " + str(US_total_cases[-1]) + "\nDeaths: " + str(US_total_dead[-1]) + "\n\n"
              + dates[-1] + "\nCases: " + str(US_case[-1]) + "\nDeaths: " + str(US_dead[-1]), title_fontsize=title_size,
        loc='center left', bbox_to_anchor=(1.05, 0.5), facecolor=background_color, edgecolor=background_color)

    plt.subplots_adjust(left=0.05, bottom=0.03, right=0.80, top=0.970, hspace=0.13)
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.show()


if __name__ == '__main__':
    main()
