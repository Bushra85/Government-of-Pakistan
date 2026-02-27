import streamlit as st

# ===================== PAGE CONFIG =====================
st.set_page_config(
    page_title="Government & Politics of Pakistan",
    layout="wide"
)

st.title("🇵🇰 Government & Politics of Pakistan (1947–Present)")
st.markdown("### Complete Constitutional, Political, Martial Law & Leaders Analysis")
st.markdown("---")

# ===================== SELECT PHASE =====================
phase = st.selectbox(
    "Select Period",
    [
        "A: 1947–1958",
        "B: 1958–1971",
        "C: 1971–1977",
        "D: 1977–1988",
        "E: 1988–1999",
        "F: 1999–Present"
    ]
)

# ===================== PHASE CONTENTS =====================

# ------------------ 1947–1958 ------------------
if phase == "A: 1947–1958":
    st.header("🟢 Pakistan: 1947–1958 (Founding Era)")

    with st.expander("📜 Constitution & Theory"):
        st.write("""
- **First Constitution (1956)** established Parliamentary democracy.
- Federal structure with Islam as state religion.
- Bicameral parliament (National Assembly + Senate).
- **Theory**: Created to unify diverse regions, provide democratic framework, and assert sovereignty after independence.
        """)

    with st.expander("⚡ Major Political Movements & Theory"):
        st.write("""
1. **Formation of Muslim League factions**
   - Cause: Regional differences within ruling party.
   - Events: Split between central leadership and provincial leaders.
   - Result: Weakening of parliamentary cohesion.
   - Theory: Early political fragmentation threatened stability.

2. **Provincial autonomy demands**
   - Cause: Sindh, NWFP, and East Pakistan sought greater rights.
   - Events: Regional protests and petitions.
   - Result: Political negotiations, but central authority remained dominant.
   - Theory: Balancing federal and provincial powers is crucial for unity.

3. **Refugee resettlement & labor strikes**
   - Cause: Mass migration post-independence.
   - Events: Riots, strikes in cities.
   - Result: Government reforms and new administrative policies.
   - Theory: Nation-building requires social and economic stabilization.
        """)

    with st.expander("👥 Key Leaders & Theory"):
        st.write("""
- **Muhammad Ali Jinnah** – Governor-General, Father of Nation.
- **Liaquat Ali Khan** – First PM; shaped early governance.
- **Iskander Mirza** – Governor-General, later first President.
- **Theory**: Leaders balanced independence challenges, nation-building, and emerging democracy.
        """)

    with st.expander("🛡 Martial Law & Theory"):
        st.write("""
- **1958**: Martial Law imposed by Iskander Mirza, ending parliamentary rule.
- **Theory**: Political instability and power struggles made civilian rule fragile.
        """)

    with st.expander("📅 Timeline & Lessons"):
        st.table({
            "Year": ["1947", "1956", "1958"],
            "Event": [
                "Pakistan gained independence",
                "First Constitution adopted",
                "First Martial Law by Iskander Mirza"
            ]
        })
        st.info("Lesson: Early democratic institutions needed stability and strong constitutional norms.")

# ------------------ 1958–1971 ------------------
elif phase == "B: 1958–1971":
    st.header("🟡 Pakistan: 1958–1971 (Ayub & Yahya Era)")

    with st.expander("📜 Constitution & Theory"):
        st.write("""
- **1962 Constitution** introduced Presidential system by General Ayub Khan.
- Unicameral legislature, Basic Democracies system.
- Strong central authority; limited political party role.
- **Theory**: Centralized power aimed to ensure stability, but weakened democratic representation.
        """)

    with st.expander("⚡ Major Political Movements & Theory"):
        st.write("""
1. **1965 Presidential Election**
   - Cause: Ayub Khan vs Fatima Jinnah
   - Events: Basic Democracies system used for indirect voting.
   - Result: Ayub won; opposition alleged rigging.
   - Theory: Electoral legitimacy is essential for democratic stability.

2. **1966 Six Points Movement**
   - Cause: Sheikh Mujibur Rahman demanded East Pakistan autonomy.
   - Events: Political campaign & public rallies.
   - Result: Widened East-West Pakistan divide.
   - Theory: Regional inequalities can threaten national unity.

3. **1968–69 Anti-Ayub Movement**
   - Cause: Economic inequality, authoritarianism.
   - Events: Strikes, student protests, civil disobedience.
   - Result: Ayub Khan resigned.
   - Theory: Citizen mobilization pressures authoritarian regimes to change policies.
        """)

    with st.expander("👥 Key Leaders & Theory"):
        st.write("""
- **Ayub Khan** – President, introduced economic reforms, authoritarian tendencies.
- **Fatima Jinnah** – Opposition leader, symbol of democracy.
- **Sheikh Mujibur Rahman** – Awami League, East Pakistan autonomy.
- **Yahya Khan** – Took over after Ayub; imposed Second Martial Law.
- **Theory**: Leadership decisions shaped centralization vs autonomy debates.
        """)

    with st.expander("🛡 Martial Law & Theory"):
        st.write("""
- **1958**: First Martial Law by Ayub Khan
- **1969**: Second Martial Law by Yahya Khan
- **Theory**: Military interventions became a recurring pattern due to weak political institutions.
        """)

    with st.expander("📅 Timeline & Lessons"):
        st.table({
            "Year": ["1958", "1962", "1965", "1966", "1968–69", "1969"],
            "Event": [
                "First Martial Law",
                "1962 Constitution enforced",
                "Presidential Election",
                "Six Points Movement",
                "Anti-Ayub Protests",
                "Second Martial Law"
            ]
        })
        st.info("Lesson: Political alienation in East Pakistan highlighted need for federal equity.")

# ------------------ 1971–1977 ------------------
elif phase == "C: 1971–1977":
    st.header("🔵 Pakistan: 1971–1977 (Zulfiqar Ali Bhutto Era)")

    with st.expander("📜 Constitution & Theory"):
        st.write("""
- **1973 Constitution**: Restored Parliamentary democracy after 1971 crisis.
- Federal structure, bicameral parliament, Islam as state religion.
- **Theory**: Rebuilt unity after Bangladesh separation, institutionalized democracy.
        """)

    with st.expander("⚡ Major Political Movements & Theory"):
        st.write("""
1. **1973 Constitutional Consensus**
   - Cause: Need to stabilize Pakistan after 1971 separation.
   - Events: All parties discussed and agreed on new constitution.
   - Result: Constitution passed unanimously.
   - Theory: Consensus among parties strengthens democratic framework.

2. **Pakistan National Alliance (PNA) 1977**
   - Cause: Allegations of election rigging by Bhutto.
   - Events: Nationwide protests, strikes, opposition alliance formed.
   - Result: Political instability → military intervention.
   - Theory: Opposition unity can challenge ruling party, but may provoke authoritarian response.

3. **Student & Civil Movements**
   - Cause: Inflation, unemployment, and political dissatisfaction.
   - Events: Campus protests, city-wide demonstrations.
   - Result: Added pressure on government, heightened political polarization.
   - Theory: Grassroots activism impacts national political stability.
        """)

    with st.expander("👥 Key Leaders & Theory"):
        st.write("""
- **Zulfiqar Ali Bhutto** – Introduced 1973 Constitution, nationalization, Islamic reforms.
- **General Zia-ul-Haq** – Army Chief; later imposed Martial Law.
- **PNA Alliance** – Religious and opposition parties demanding fair elections.
- **Theory**: Leadership conflict and political polarization led to fragile democracy.
        """)

    with st.expander("🛡 Martial Law & Theory"):
        st.write("""
- **5 July 1977**: Third Martial Law imposed by Zia-ul-Haq.
- **Theory**: Political instability and protests allowed military to seize control.
        """)

    with st.expander("📅 Timeline & Lessons"):
        st.table({
            "Year": ["1973", "1977", "5 July 1977", "1979", "1985"],
            "Event": [
                "1973 Constitution Passed",
                "Election Controversy",
                "Martial Law Imposed",
                "Bhutto Executed",
                "Partial Restoration of Constitution"
            ]
        })
        st.info("Lesson: Consensus, inclusion, and management of opposition are vital for constitutional stability.")

# ------------------ 1977–1988 ------------------
elif phase == "D: 1977–1988":
    st.header("🟠 Pakistan: 1977–1988 (Zia-ul-Haq Era)")

    with st.expander("📜 Constitution & Governance"):
        st.write("""
- Constitution suspended; military-authoritarian rule.
- 8th Amendment strengthened President over PM.
- 1985 Non-party elections allowed limited civilian rule.
- **Theory**: Military used governance structures to maintain control, Islamization policies reshaped legal system.
        """)

    with st.expander("⚡ Major Political Movements & Theory"):
        st.write("""
1. **MRD (1981)**
   - Cause: Opposition demanded end of Martial Law.
   - Events: Nationwide protests, arrests, civil disobedience.
   - Result: Limited political reforms, kept military alert.
   - Theory: Civil pressure gradually restored political awareness and democracy.

2. **Civil society & student activism**
   - Cause: Suppression of freedoms.
   - Events: Lawyers, women, and student movements.
   - Result: Laid foundations for democracy restoration.
   - Theory: Organized civil movements can influence authoritarian regimes.
        """)

    with st.expander("👥 Key Leaders & Theory"):
        st.write("""
- **Zia-ul-Haq** – Martial Law Administrator and President.
- **Benazir Bhutto** – PPP leader; symbol of democracy.
- **Nusrat Bhutto** – Co-led PPP opposition.
- **Theory**: Leadership shaped resistance and resilience of democratic forces.
        """)

    with st.expander("🛡 Martial Law & Theory"):
        st.write("""
- 3rd Martial Law: 5 July 1977 – 1988
- **Theory**: Military rule replaced parliamentary democracy; civilian governance limited.
        """)

    with st.expander("📅 Timeline & Lessons"):
        st.table({
            "Year": ["1977", "1979", "1981", "1985", "1985", "1988"],
            "Event": [
                "Martial Law imposed",
                "Bhutto executed",
                "MRD launched",
                "Non-party elections",
                "8th Amendment passed",
                "Zia died; democracy restored"
            ]
        })
        st.info("Lesson: Authoritarianism may create short-term stability but weakens democratic culture.")

# ------------------ 1988–1999 ------------------
elif phase == "E: 1988–1999":
    st.header("🟣 Pakistan: 1988–1999 (Democratic Instability)")

    with st.expander("📜 Constitution & Theory"):
        st.write("""
- 1973 Constitution restored; Article 58(2)(b) allowed President to dissolve assemblies.
- Civilian democracy weak due to frequent dismissals.
- **Theory**: Constitutional provisions can strengthen or weaken democracy depending on leadership behavior.
        """)

    with st.expander("⚡ Major Political Movements & Theory"):
        st.write("""
1. **Civilian supremacy campaigns**
   - Cause: Presidents dissolved assemblies under Article 58(2)(b)
   - Events: Political protests by PPP and PML-N
   - Result: Highlighted weakness of democratic institutions
   - Theory: Strong institutions needed to prevent arbitrary use of power

2. **Protests against government dismissals**
   - Cause: Repeated removal of PMs
   - Events: Demonstrations, civil activism
   - Result: Temporary public pressure but political instability continued
   - Theory: Citizen engagement can check executive abuse, but constitutional loopholes matter
        """)

    with st.expander("👥 Key Leaders & Theory"):
        st.write("""
- **Benazir Bhutto** – PM twice, faced dismissals.
- **Nawaz Sharif** – PM twice, dismissed once.
- **Ghulam Ishaq Khan** – President; used Article 58(2)(b).
- **Theory**: Leaders’ rivalry affected democratic continuity.
        """)

    with st.expander("🛡 Martial Law & Theory"):
        st.write("No formal Martial Law, but military influence remained behind the scenes.")

    with st.expander("📅 Timeline & Lessons"):
        st.table({
            "Year": ["1988", "1990", "1993", "1996", "1997", "1999"],
            "Event": [
                "Zia dies; Benazir elected PM",
                "Benazir dismissed; Nawaz Sharif elected",
                "Nawaz dismissed; Benazir elected again",
                "Benazir dismissed; caretaker government",
                "Nawaz Sharif returns as PM",
                "Military coup by Pervez Musharraf"
            ]
        })
        st.info("Lesson: Weak democratic institutions and constitutional loopholes can destabilize governance.")

# ------------------ 1999–Present ------------------
elif phase == "F: 1999–Present":
    st.header("🔴 Pakistan: 1999–Present (Musharraf & Modern Era)")

    with st.expander("📜 Constitution & Governance"):
        st.write("""
- Military coup by **Pervez Musharraf** (1999); Martial Law imposed.
- Legal Framework Order (LFO) modified constitution; 18th Amendment (2010) restored Parliament’s power.
- **Theory**: Constitutional amendments shape balance of power between executive and legislature.
        """)

    with st.expander("⚡ Major Political Movements & Theory"):
        st.write("""
1. **Lawyers’ Movement (2007–2009)**
   - Cause: Suspension of Chief Justice Iftikhar Muhammad Chaudhry
   - Events: Nationwide protests, rallies, media campaigns
   - Result: Judiciary restored; strengthened rule of law
   - Theory: Strong civil society and judiciary reinforce constitutional democracy

2. **Civil society democratic movements**
   - Cause: Military dominance in politics
   - Events: Media activism, NGO campaigns
   - Result: Political pressure on Musharraf; democracy restored in 2008
   - Theory: Citizen and media activism can influence military regimes
        """)

    with st.expander("👥 Key Leaders & Theory"):
        st.write("""
- **Pervez Musharraf** – Army Chief turned President; introduced reforms but controlled political space.
- **Benazir Bhutto** – Returned 2007, assassinated; symbol of democracy.
- **Nawaz Sharif** – Political leader, returned 2007; won 2013 elections.
- **Theory**: Leadership choices influence democratization, judicial independence, and constitutional reform.
        """)

    with st.expander("🛡 Martial Law & Theory"):
        st.write("""
- 1999 Martial Law under Musharraf until 2001 (Chief Executive → President).
- Democracy restored in 2008; military influence gradually reduced.
- **Theory**: Military rule may stabilize governance temporarily but risks long-term democratic development.
        """)

    with st.expander("📅 Timeline & Lessons"):
        st.table({
            "Year": ["1999", "2001", "2002", "2007", "2008", "2010"],
            "Event": [
                "Military coup by Musharraf; Nawaz Sharif removed",
                "Musharraf assumes Presidency",
                "General elections under Musharraf",
                "Lawyers’ Movement & Benazir assassination",
                "Democracy restored; Musharraf resigns",
                "18th Amendment strengthens Parliament"
            ]
        })
        st.info("Lesson: Judicial empowerment, constitutional reform, and civil activism strengthen democracy.")

# ===================== END =====================
st.markdown("---")
st.info(
    '“Democracy is the backbone of Pakistan’s progress, yet history shows the struggle between civilian rule and military intervention is continuous.”')
st.markdown("### Website Owner: Surhan Mishal")