import pandas as pd

df = pd.read_csv(r"dataset\covid_vaccine_statewise.csv")

print(df)

df.rename(
    columns={
        "Updated On": "date_updated",
        "State": "state",
        "Total Doses Administered": "ttl_doses_adm",
        "Sessions": "sessions",
        " Sites ": "sites",  # note: there’s extra space around 'Sites'
        "First Dose Administered": "first_dose_adm",
        "Second Dose Administered": "second_dose_adm",
        "Male (Doses Administered)": "male_doses_adm",
        "Female (Doses Administered)": "female_doses_adm",
        "Transgender (Doses Administered)": "trans_doses_adm",
        " Covaxin (Doses Administered)": "covaxin_doses_adm",
        "CoviShield (Doses Administered)": "covishield_doses_adm",
        "Sputnik V (Doses Administered)": "sputnik_doses_adm",
        "AEFI": "aefi",
        "18-44 Years (Doses Administered)": "age_18_44_doses_adm",
        "45-60 Years (Doses Administered)": "age_45_60_doses_adm",
        "60+ Years (Doses Administered)": "age_60plus_doses_adm",
        "18-44 Years(Individuals Vaccinated)": "age_18_44_indiv_vac",
        "45-60 Years(Individuals Vaccinated)": "age_45_60_indiv_vac",
        "60+ Years(Individuals Vaccinated)": "age_60plus_indiv_vac",
        "Male(Individuals Vaccinated)": "male_indiv_vac",
        "Female(Individuals Vaccinated)": "female_indiv_vac",
        "Transgender(Individuals Vaccinated)": "trans_indiv_vac",
        "Total Individuals Vaccinated": "total_indiv_vac",
    },
    inplace=True,
)

df["date_updated"] = pd.to_datetime(df["date_updated"])

cols_to_drop = [
    "sessions",
    "sites",
    "aefi",
    "covaxin_doses_adm",
    "covishield_doses_adm",
    "sputnik_doses_adm",
]

df.drop(columns=cols_to_drop, inplace=True, axis=1)


output_path = (
    r"cleaned_data/clean_vaccine_statewise.csv"
)

df.to_csv(output_path, index=False)
