## Permanent Medical Exemption per Year for all school types
sns.set(style="whitegrid")
PME_year_axis = sns.boxplot(x='year', y='pPME', data=PermanentMedicalExemption_percent)
PME_year_axis.set(xlabel='Year', ylabel='Number of Permanent Medical Exemptions', title='Permanent Medical Exemptions per Year')
plt.xticks(rotation=90)
plt.show()

## Permanent Medical Exemption per County for all school types
PME_county_axis = sns.boxplot(x='COUNTY', y='pPME', data=PermanentMedicalExemption_percent)
PME_county_axis.set(xlabel='County', ylabel='Number of Permanent Medical Exemptions', title='Permanent Medical Exemptions per County')
plt.xticks(rotation=90)
plt.show()

## PME rates per school
PME_school = student_df.groupby('SCHOOL').agg(sum_n=('n', sum), sum_PME=('nPME', sum)).reset_index()
PME_school['pPME'] = PME_school['sum_PME'] / PME_school['sum_n'] * 100
PME_school['pn'] = 100
PME_school.sort_values(by=['pPME'], ascending=False, inplace=True)

figure = plt.figure(figsize=(6, 15))
ax = figure.subplots()
sns.set_color_codes("pastel")
sns.barplot(x='pn', y='SCHOOL', data=PME_school.head(20), color='b', label='Total number of students')
sns.set_color_codes("muted")
sns.barplot(x='pPME', y='SCHOOL', data=PME_school.head(20),color='b', label='Number of Permanent Medical Exemptions')
ax.legend(ncol=2, loc="lower right", frameon=True)
sns.despine(left=True, bottom=True)

plt.show()


## Personal Belief Exemption per Year for all school types
PBE_year_axis = sns.boxplot(x='year', y='pPBE', data=PersonalBeliefsExemption_percent)
PBE_year_axis.set(xlabel='Year', ylabel='Number of Personal Belief Exemptions', title='Personal Belief Exemptions per Year')
plt.xticks(rotation=90)
plt.show()

## Personal Belief Exemption per County for all school types
PBE_county_axis = sns.boxplot(x='COUNTY', y='pPBE', data=PersonalBeliefsExemption_percent)
PBE_county_axis.set(xlabel='County', ylabel='Number of Personal Belief Exemptions', title='Personal Belief Exemptions per County')
plt.xticks(rotation=90)
plt.show()

## PBE rates per school
PersonalBeliefsExemption_perSchool = student_df.groupby('SCHOOL').apply(lambda x: x.nPBE.sum()/x.n.sum()*100).to_frame('pPBE').reset_index()
PersonalBeliefsExemption_perSchool['pn'] = 100
PersonalBeliefsExemption_perSchool.sort_values(by=['pPBE'], ascending=False, inplace=True)

figure = plt.figure(figsize=(6, 15))
ax = figure.subplots()
sns.set_color_codes("pastel")
sns.barplot(x='pn', y='SCHOOL', data=PersonalBeliefsExemption_perSchool.head(20), color='b', label='Total number of students')
sns.set_color_codes("muted")
sns.barplot(x='pPBE', y='SCHOOL', data=PersonalBeliefsExemption_perSchool.head(20),color='b', label='Number of Personal Beliefs Exemptions')
ax.legend(ncol=2, loc="lower right", frameon=True)
sns.despine(left=True, bottom=True)

plt.show()

### DTP immunization rates

## DTP immunization rates  per Year for all school types
DTP_year_axis = sns.boxplot(x='year', y='pDTP', data=DTP_vaccinated_percent)
DTP_year_axis.set(xlabel='Year', ylabel='DTP immunization rates', title='DTP immunization rates per Year')
plt.xticks(rotation=90)
plt.show()

## DTP immunization rates  per County for all school types
DTP_county_axis = sns.boxplot(x='COUNTY', y='pDTP', data=DTP_vaccinated_percent)
DTP_county_axis.set(xlabel='County', ylabel='DTP immunization rates', title='DTP immunization rates per County')
plt.xticks(rotation=90)
plt.show()

## Lowest DTP rates per school
DTP_perSchool = student_df.groupby('SCHOOL').apply(lambda x: x.nDTP.sum()/x.n.sum()*100).to_frame('pDTP').reset_index()
DTP_perSchool['pn'] = 100
DTP_perSchool.sort_values(by=['pDTP'], ascending=True, inplace=True)

figure_DTPperSchool = plt.figure(figsize=(6, 15))
ax_DTPperSchool = figure_DTPperSchool.subplots()
sns.set_color_codes("pastel")
sns.barplot(x='pn', y='SCHOOL', data=DTP_perSchool.head(20), color='b', label='Total number of students')
sns.set_color_codes("muted")
sns.barplot(x='pDTP', y='SCHOOL', data=DTP_perSchool.head(20),color='b', label='DTP immunization rate')
ax_DTPperSchool.legend(ncol=2, loc="lower right", frameon=True)
ax_DTPperSchool.set(ylabel='Schools', title='DTP immunization rates in schools')
sns.despine(left=True, bottom=True)

plt.show()

### Polio immunization rates

## Polio immunization rates  per Year for all school types
Polio_year_axis = sns.boxplot(x='year', y='pPolio', data=Polio_vaccinated_percent)
Polio_year_axis.set(xlabel='Year', ylabel='Polio immunization rates', title='Polio immunization rates per Year')
plt.xticks(rotation=90)
plt.show()

## Polio immunization rates  per County for all school types
Polio_county_axis = sns.boxplot(x='COUNTY', y='pPolio', data=Polio_vaccinated_percent)
Polio_county_axis.set(xlabel='County', ylabel='Polio immunization rates', title='Polio immunization rates per County')
plt.xticks(rotation=90)
plt.show()

## Lowest Polio rates per school
Polio_perSchool = student_df.groupby('SCHOOL').apply(lambda x: x.nPolio.sum()/x.n.sum()*100).to_frame('pPolio').reset_index()
Polio_perSchool['pn'] = 100
Polio_perSchool.sort_values(by=['pPolio'], ascending=True, inplace=True)

figure_PolioperSchool = plt.figure(figsize=(6, 15))
ax_PolioperSchool = figure_PolioperSchool.subplots()
sns.set_color_codes("pastel")
sns.barplot(x='pn', y='SCHOOL', data=Polio_perSchool.head(20), color='b', label='Total number of students')
sns.set_color_codes("muted")
sns.barplot(x='pPolio', y='SCHOOL', data=Polio_perSchool.head(20),color='b', label='Polio immunization rate')
ax_PolioperSchool.legend(ncol=2, loc="lower right", frameon=True)
ax_PolioperSchool.set(ylabel='Schools', title='Polio immunization rates in schools')
sns.despine(left=True, bottom=True)

plt.show()

### MMR immunization rates

## MMR immunization rates  per Year for all school types
MMR_year_axis = sns.boxplot(x='year', y='pMMR', data=MMR_vaccinated_percent)
MMR_year_axis.set(xlabel='Year', ylabel='MMR immunization rates', title='MMR immunization rates per Year')
plt.xticks(rotation=90)
plt.show()

## MMR immunization rates  per County for all school types
MMR_county_axis = sns.boxplot(x='COUNTY', y='pMMR', data=MMR_vaccinated_percent)
MMR_county_axis.set(xlabel='County', ylabel='MMR immunization rates', title='MMR immunization rates per County')
plt.xticks(rotation=90)
plt.show()

## Lowest MMR rates per school
MMR_perSchool = student_df.groupby('SCHOOL').apply(lambda x: x.nMMR.sum()/x.n.sum()*100).to_frame('pMMR').reset_index()
MMR_perSchool['pn'] = 100
MMR_perSchool.sort_values(by=['pMMR'], ascending=True, inplace=True)

figure_MMRperSchool = plt.figure(figsize=(6, 15))
ax_MMRperSchool = figure_MMRperSchool.subplots()
sns.set_color_codes("pastel")
sns.barplot(x='pn', y='SCHOOL', data=MMR_perSchool.head(20), color='b', label='Total number of students')
sns.set_color_codes("muted")
sns.barplot(x='pMMR', y='SCHOOL', data=MMR_perSchool.head(20),color='b', label='MMR immunization rate')
ax_MMRperSchool.legend(ncol=2, loc="lower right", frameon=True)
ax_MMRperSchool.set(ylabel='Schools', title='Lowest MMR immunization rates in schools')
sns.despine(left=True, bottom=True)

plt.show()
