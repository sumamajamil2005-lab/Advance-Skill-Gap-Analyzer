import streamlit as st
import os
from additional.extra_support import extract_and_save_resume 
from matcher.skill_matcher import skill_matcher
from parsers.file_loader import file_loader
from parsers.skill_parser import generic_parser
from writer.report_writer import Report_writer
from additional.recommendation import get_recommendation
from additional.skill_level import get_skill_level
from additional.extra_support import extract_and_save_resume

def main():
    MASTER_SKILLS = "skills/skill_lists.txt"
    JD_FILE = "data/job_description.txt"
    RESUME_FILE = "data/resume.txt"
    REPORT_FILE = "output/report.txt"






    st.set_page_config(page_title="Skill Gap Analyzer", layout="centered")

    st.title("Skill Gap Analyzer")

    # --- SECTION 1: JOB DESCRIPTION ---
    st.subheader("Step 1: Job Description")
    jd_input = st.text_area("Paste the Job Description (JD) here", height=150)

    if st.button("Save Job Description"):
        if jd_input:
            if not os.path.exists("data"):
                os.makedirs("data")
            # JD ko file mein save karna
            with open("data/job_description.txt", "w", encoding="utf-8-sig") as f:
                f.write(jd_input)
            st.success("Job Description saved to 'data/job_description.txt'!")
        else:
            st.warning("Please enter some text first.")

    st.divider()

    # --- SECTION 2: RESUME UPLOAD ---
    st.subheader("Step 2: Upload Resume")
    uploaded_file = st.file_uploader("Choose a PDF or DOCX file", type=["pdf", "docx"])

    if uploaded_file is not None:
        # 1. File ko data folder mein save karo
        temp_path = os.path.join("data", uploaded_file.name)
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # 2. Extract and Save Text (Tera purana function)
        with st.spinner('Extracting text from resume...'):
            success = extract_and_save_resume(temp_path)
        
        if success:
            st.success(f"Resume text extracted and saved to 'data/resume.txt'!")
            
            # --- FINAL TRIGGER ---
            if st.button("🚀 Analyze Skill Gap Now"):
                st.info("Analysis report is being generated...")
                content = file_loader(MASTER_SKILLS)
                valid_jd = generic_parser(JD_FILE , content)
                valid_resume = generic_parser(RESUME_FILE , content)
                matched , missed  , points = skill_matcher(valid_jd , valid_resume)
                recommend = get_recommendation(points , missed)
                level = get_skill_level(points)
                Report_writer(REPORT_FILE , matched, missed , points,level , recommend, valid_jd )


                st.divider()
                st.subheader("📊 Skill Gap Analysis Report")


                with st.container():

                    st.info("### SKILL GAP ANALYSIS COMPLETE")
                    

                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric(label="Match Score", value=f"{round(points , 2)}%")
                    with col2:
                        st.write(f"**OVERALL MATCH**: {round(points , 2)}%\n")
                        st.write(f"**CANDIDATE LEVEL:** {level}")
                        st.write(f"**ADVICE:** {recommend}")
                        st.write("---")
                    
                    c1, c2 = st.columns(2)
                    with c1:
                        st.write("### ✅ Matched")
                        if matched:
                            matched_names = [s['name'] for s in matched]
                            st.write(f"\n-> MATCHED SKILLS: {', '.join(matched_names)}\n")
                
                            full_matches = [s['name'] for s in matched if s['type'] == 'Full']
                            partial_matches = [s['name'] for s in matched if s['type'] == 'Partial']
                            semantic_matches = [s['name'] for s in matched if s['type'] == 'Semantic']

                            st.write("   ∟ FULL MATCH: " + (", ".join(full_matches) if full_matches else "None") + "\n")
                            st.write("   ∟ PARTIAL MATCH: " + (", ".join(partial_matches) if partial_matches else "None") + "\n")
                            st.write("   ∟ CONCEPTUAL (AI): " + (", ".join(semantic_matches) if semantic_matches else "None") + "\n")
                        else:
                            st.write("None")

                    with c2:
                        st.write("### ❌ Missing")
                        if missed:
                            # Same logic missed ke liye
                            missed_names = [str(m['name']) if isinstance(m, dict) else str(m) for m in missed]
                            st.write(", ".join(missed_names))
                        else:
                            st.write("None")

                            

                    st.success(f"✅ Detailed report saved to: `output/report.txt`")

                st.divider()

        else:
            st.error("Could not extract text. Check the file format.")

if __name__ == "__main__":
    main()