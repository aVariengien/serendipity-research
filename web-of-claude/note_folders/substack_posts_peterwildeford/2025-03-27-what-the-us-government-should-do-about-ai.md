# What the US government should do about AI

*Over two dozen recommendations to improve national security*

Published: 2025-03-27
Source: https://peterwildeford.substack.com/p/what-the-us-government-should-do

---

[![](https://substackcdn.com/image/fetch/$s_!eoaW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F130cfd0b-1bd8-4fcb-8794-abeb4e725b1d_1536x1024.png)](https://substackcdn.com/image/fetch/$s_!eoaW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F130cfd0b-1bd8-4fcb-8794-abeb4e725b1d_1536x1024.png)

The Trump Administration is crafting an AI Action Plan and [requested public comment](https://www.federalregister.gov/documents/2025/02/06/2025-02305/request-for-information-on-the-development-of-an-artificial-intelligence-ai-action-plan). I previously covered [how Google, Anthropic, and OpenAI were responding](https://peterwildeford.substack.com/p/ai-titans-clash-over-visions-for) and now I want to cover what I think we should do. I work at the Institute for AI Policy and Strategy and **[we recently submitted our response to the AI Action Plan as well](https://www.iaps.ai/research/ostp-rfi)**. What follows is my summary of our response.

**We recommended the AI Action Plan include three key areas:**

* **Build trust in American AI**: Establish AI systems that governments, businesses, and consumers can trust through enhanced security and reliability standards. Leverage federal capabilities to address critical market gaps and secure AI supply chains against malicious disruption.

* **Deny foreign adversary access to advanced computing technology:** Maintain America's technological advantage by controlling semiconductor exports to adversaries, forcing them to choose between research advancement and deployment. Coordinate across government agencies to ensure effective implementation of these controls.

* **Understand and respond to changing capabilities**: The United States needs the ability and agility to respond at speed as technology evolves. By developing the systems and standards now, the Administration creates optionality for responding in the future. Develop evaluation standards to assess emerging AI systems and their national security implications. Create coordinated visibility across government, industry, and research institutions to promote beneficial AI while addressing security concerns.

#

# Build trust in American AI

Systems that diagnose diseases, offer autonomous transportation, and manage critical infrastructure must be both secure and reliable to ensure widespread adoption.

From aviation protocols to encryption standards, the US government has repeatedly pioneered research and frameworks later adopted throughout industry that has enabled innovation to thrive. We think the same should be done for AI.

We recommend the US government:

* **Direct federal civilian and defense research agencies to prioritize funding research that helps improve the security and reliability of AI models.** OSTP, with support from OMB, should include a list of critical AI security technologies in vehicles such as the annual multi-agency R&D priorities memoranda and the next update of the National R&D Strategic Plan, as well as work with AI R&D funders to develop technology roadmaps that detail related technical benchmarks and milestones, capability development timelines, resource requirements, and stakeholder roles and responsibilities.
* **Prioritize AI research that the private sector might overlook** such as on [hardware security](https://www.rand.org/pubs/research_reports/RRA2849-1.html), [multi-agent interaction safety](https://arxiv.org/abs/2311.10538), [cybersecurity for AI models](https://metr.org/blog/2024-11-12-rogue-replication-threat-model/), and [evaluation methods](https://arxiv.org/abs/2411.15114) for safety-critical uses.
* The US National Labs have strong expertise and classified compute. **We must use the DOE to create dedicated AI research hubs that provide researchers access to secure testing environments** critical for staying ahead of threats.

We also must be on guard that foreign actors will increasingly target private sector AI assets with [model theft](https://www.rand.org/pubs/research_reports/RRA2849-1.html), [data poisoning](https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/data-poisoning/), and [model trojans](https://arxiv.org/abs/2401.05566). We recommend the US government:

* **Direct NIST, in coordination with CISA and NSA, to develop comprehensive standards for securing AI systems**, including guidance on secure development practices (i.e. NIST SP 800-218A), vulnerability management in models and scaffolding, deployment configurations, and AI agent-specific security controls.
* **Direct NIST to develop standards and guidance for AI system reliability**, focusing on reliable design methodologies, robust testing frameworks, and operational deployment considerations to ensure consistent performance and accuracy across varied production environments.
* **Direct sector-specific agencies, in coordination with NIST, to develop tailored AI reliability guidelines** addressing unique operational requirements, risk profiles, and compliance considerations for their respective industries.

* **Direct CISA to track and catalog AI security vulnerabilities** by either updating the Common Vulnerabilities and Exposure (CVE) program or develop a new process specifically designed to improve the identification and mitigation of AI-related cybersecurity threats.
* **Direct NIST to update the National Vulnerability Database (NVD) to better accommodate and categorize AI-specific vulnerabilities**, enhancing the repository's ability to serve as a comprehensive resource for AI security risks.
* **Direct NIST to develop security standards for model weights** (equivalent to SL4 and SL5 as outlined by the [RAND Corporation](https://www.rand.org/pubs/research_reports/RRA2849-1.html)) and other critical assets beyond model weights (i.e. algorithms and training data). Prioritize research that supports the development of technologies required to meet or exceed the SL4 and SL5 security standards.

* **Direct relevant agencies to expand AI security research efforts and establish competitive initiatives to prevent model sabotage and tampering**, for example by broadening IARPA's TrojAI program to include comprehensive defensive controls and launching cross-sector Red Team R&D programs that perform adversarial testing throughout the AI model lifecycle.

* **Designate AI and Advanced Computing (AIAC) as a critical infrastructure sector.** The sector should include stakeholders in the AI supply chain (i.e. AI developers, cloud hyperscalers, semiconductors manufacturers). Designate DHS as the SRMA for the AIAC sector to provide services, technical assistance, and coordinated public-private collaboration efforts.
* **Direct the intelligence community to prioritize identifying and analyzing nation-state efforts to target the AIAC sector.**

Additionally, to be an effective partner to industry, Federal Government agencies need clear roles, specialized expertise, and dedicated resources. The private sector should not have to navigate a byzantine and uncoordinated maze of government agencies to find support.

We recommend the US government:

* **Issue a White House policy directive that identifies and clarifies Federal agencies' roles and responsibilities related to AI and advanced computing.** The directive should establish lead and supporting roles to address AI policy issues, including AI evaluations, standards development, and supply chain security. This should include designating a primary federal government point of contact with private sector AI developers to facilitate voluntary testing of dual-use foundation models.

* **Establish a US government AI center, a yet-to-be-named centralized node somewhere within US governmnt. It’s function would be to enable AI use by evaluating emerging AI capabilities, developing assurance standards, and fostering close collaboration with industry.** Key functions should include:

  + Advancing AI measurement and evaluation science, providing both the private and public sector with the tools to identify and understand AI’s economic opportunities and potentially dangerous capabilities.
  + Conducting technical evaluations by working with AI developers.
  + Developing and promoting standards and guidance, including assurance standards that improve the security and reliability of AI systems.
  + Serving as a source of expertise and coordinating with other Federal Agencies, including helping sector-specific agencies promote safe AI deployment within their respective sectors.
  + Engaging with external stakeholders, including AI developers, Standards Development Organizations (SDOs), and the AI institutes of other countries.
  + *This could be accomplished by restructuring, re-housing, or replacing the US AI Safety Institute (US AISI), but it is critical that the U.S. government have a center of gravity for these functions.*

####

# Deny foreign adversary access to advanced computing technology

**American technology must not be used to hurt Americans.** CCP theft of AI and civil-military fusion is concerning. Semiconductor export controls will be critical.

[Weak and insufficient controls in the past are what enabled DeepSeek today and why China is only 6 months behind the US](https://peterwildeford.substack.com/p/ten-takes-on-deepseek). Strengthening and enforcing these controls will build a solid American lead. Effective controls today compound to lasting security tomorrow.

However, sufficient export control enforcement requires a whole-of-government approach. The Bureau of Industry and Security (BIS) cannot single-handedly counter smuggling, identify technical loopholes, and lead international coalitions. Effective implementation demands coordinated action across the intelligence community, the State Department, the Department of Homeland Security, and technical agencies like NIST.

We recommend the US government:

* **Establish a Joint Federal Task Force, led by a revitalized BIS**, focused on [stopping the diversion of AI chips and illegal tech transfer](https://www.aipolicybulletin.org/articles/ai-chip-smuggling-is-the-default-not-the-exception) of information relevant to advanced AI semiconductor manufacturing, such as electronic design automation (EDA) software piracy. The administration should use all relevant policy tools and authorities to enforce semiconductor export controls. The Task Force should include ODNI, DOJ, State, and DHS, and prioritize improved interagency coordination between the IC and BIS.
* **Direct ODNI to collect and share relevant intelligence with BIS** to strengthen export control enforcement, including through mapping smuggling networks and weak points in the AI chip distribution network. This would enable BIS to target enforcement more efficiently.
* **Direct NIST to [collaborate with industry](https://www.cnas.org/publications/reports/technology-to-secure-the-ai-chip-supply-chain-a-primer) to identify [hardware security features](https://www.cnas.org/publications/reports/secure-governable-chips) and other technology that can support export control enforcement and deter smuggling.** This should include commissioning a feasibility study of delay-based [location verification](https://www.iaps.ai/research/location-verification-for-ai-chips) for AI chips and creating a centralized chip registry pilot database within BIS. These features could enable more efficient enforcement generally and allow industry to export to higher-risk destinations, such as the Middle East, while reducing the risk of chips being smuggled to China.
* **Direct BIS to expand export controls to include NVIDIA H20 chips** and equivalents, while also reviewing whether some consumer GPUs need to be more strongly controlled.
* **Establish a BIS whistleblower program** to incentivize reports of export violations, funded via penalties levied on violators.

* **Revise [the AI diffusion rule](https://www.rand.org/pubs/perspectives/PEA3776-1.html) to create clear criteria for countries to gain 'Tier 1' status**, e.g. by improving their export control enforcement practices, to ensure the right set of countries are in the Tier 1 group and incentivize Tier 2 countries to better enact controls.
* **Direct the Department of Commerce to establish reporting requirements for cloud computing providers** regarding sales metrics and transaction details with Chinese entities, including [customer verification procedures](https://arxiv.org/abs/2310.13625) and compliance with export control.

# Understand and Prepare to Respond to Changing AI Capabilities

While experts differ on the timeline, we are likely to see continued major breakthroughs during the current Administration.

We already see AI systems that can [identify zero-day cyber vulnerabilities](https://team-atlanta.github.io/blog/post-asc-sqlite/) and conduct [complex multi-stage cyberattacks](https://arxiv.org/pdf/2501.16466). Additionally, OpenAI and Anthropic warn future models may soon guide novices in bioweapons creation. Monitoring AI for dual-use risks is critical. Government-industry collaboration can spot threats early, avoiding catastrophe and reactive overregulation.

[![Image](https://substackcdn.com/image/fetch/$s_!9nYz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7c0c223f-d963-4900-a6a3-f102332e7da5_1042x602.jpeg "Image")](https://substackcdn.com/image/fetch/$s_!9nYz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7c0c223f-d963-4900-a6a3-f102332e7da5_1042x602.jpeg)

This could enable significantly more advanced AI attacks that we must be prepared for. **The US government regularly prepares for low-probability but high-consequence risks. AI should be no different.**

We recommend the US government:

* **Direct NIST to update AI capability evaluation standards and guidance to handle a broader range of national-security relevant capabilities beyond cybersecurity and CBRN.** These standards should be based on the latest measurement science and updated frequently to keep pace with emerging AI system capabilities. Additional key capability areas for evaluations include: agent and [multi-agent interactions](https://www.cs.toronto.edu/~nisarg/papers/Multi-Agent-Risks-from-Advanced-AI.pdf) (e.g., collusion capability between agents); model [deception](https://openai.com/index/chain-of-thought-monitoring/), [scheming](https://www.apolloresearch.ai/research/scheming-reasoning-evaluations), and [situational awareness](https://arxiv.org/abs/2412.14093); and [automated AI research and development](https://arxiv.org/abs/2411.15114) capabilities.

* **Direct NIST or other relevant federal agencies to provide guidance that helps companies encourage independent third-party testing of AI systems.** This should cover both traditional security vulnerabilities and AI-specific risks that may lead to malicious use. This could include guidance on vulnerability disclosure programs and bug bounty initiatives that [protect good-faith researchers](https://knightcolumbia.org/blog/a-safe-harbor-for-ai-evaluation-and-red-teaming) from liability, such as rules of engagement that define testing boundaries, permitted methods, and reporting procedures.

* **Direct the US government AI center, in coordination with all relevant federal agencies, to lead evaluation efforts to identify emerging frontier model capabilities that could support or threaten US national security.** This should include both classified (confidential) and unclassified (publicly available) evaluations. When appropriate, the evaluating agencies should enter into agreements with model developers to receive early access and provide feedback.
* **The administration should consider tasking specific agencies with developing domain specific evaluations** with the US government AI center supporting. For example:

  + Direct the NSA to develop classified offensive and defensive cyber capabilities evaluations.
  + Direct the National Nuclear Security Administration (NNSA) to develop classified evaluations of nuclear and radiological relevant capabilities.
  + Direct the US government AI center, in coordination with DHS and HHS, and other relevant agencies to develop classified evaluations of capabilities that could generate or exacerbate chemical and biological risks.
* **Direct ODNI to assess strategic adversaries' AI capabilities**, examining talent flows, computing resources, leadership intentions, and contingency measures for restricting adversarial AI systems when required. Classified findings should be submitted to the White House, China Select Committee, and Senate Intelligence Committee.

Quick action matters. We also recommend agile response groups to rapidly assess emerging AI threats to national security - combining academia, government, and industry for timely, expert-driven solutions.

* **The White House should establish a Rapid Emerging Assessment Council for Threats (REACT)**, able to rapidly convene cross-disciplinary subject matter experts to assess sudden, emerging, or novel AI-related threats to critical infrastructure or national security where government, industry, and academia may need to convene quickly to understand and mitigate sudden risks.

* **The US government should maintain the [Testing Risks of AI for National Security (TRAINS) Taskforce](https://www.commerce.gov/news/press-releases/2024/11/us-ai-safety-institute-establishes-new-us-government-taskforce)** and assign agency leads that will coordinate responses to reports of national security and public safety-relevant capabilities in frontier AI systems that arise from testing.

# Looking forward

We share the President’s vision for seeing AI as an opportunity for America. Advancements in AI bring enormous potential for scientific, economic, and productivity gains, and the benefits for Americans could be tremendous. However, we must also be mindful of the risks – future, more advanced AI may produce domestic market disruptions and the rise of weaponized AI attacks from U.S. adversaries. These disruptions would have profound implications for national security, geopolitical stability, and the everyday life of American citizens. The public will expect the government to understand and manage these disruptions.

**However, through smart policy, America can maintain its competitive edge in AI by supporting industry leadership while defending citizens.** The Administration has the opportunity through the AI Action Plan to set out a vision for AI that is secure, reliable, and able to achieve the promise of transformative economic and societal gains.

**[—> To learn more, Read IAPS’s plan in more detail](https://static1.squarespace.com/static/64edf8e7f2b10d716b5ba0e1/t/67da09685aa52048665ddd34/1742342504498/IAPS+OSTP+RFI.pdf)**

Subscribe if you’d like more ideas for how to navigate AI’s opportunities

Subscribe