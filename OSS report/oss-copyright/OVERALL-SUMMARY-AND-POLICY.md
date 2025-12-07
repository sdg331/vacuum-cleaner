# 1. OVERALL SUMMARY AND POLICY (전체 정리 및 정책 요약)

## 1.1 Report Objective (보고서 목적)

본 **OSS 저작권 보고서(OSS Copyright Report)**는 `vacuum-cleaner` 프로젝트 개발 과정에서 사용된 모든 오픈 소스 소프트웨어(Open Source Software, 이하 OSS)를 투명하게 공개하고, 이에 따른 법적 의무를 이행하기 위해 작성되었습니다.

본 보고서의 주요 목적은 다음과 같습니다.
1.  **고지 의무(Attribution) 준수:** MIT, Apache 2.0 등 사용된 라이선스 조건에 따라 저작권자 및 라이선스 전문을 명시합니다.
2.  **법적 리스크 관리:** 프로젝트가 제3자의 지식재산권을 침해하지 않았음을 증명하고, 라이선스 충돌(License Conflict)이 없음을 확인합니다.
3.  **투명성 확보:** 최종 사용자 및 이해관계자에게 사용된 외부 코드의 출처와 권리 관계를 명확히 제공합니다.

## 1.2 Compliance Responsibility (관리 책임 및 담당)

본 프로젝트의 OSS 컴플라이언스(규정 준수) 관리는 아래의 책임 주체에 의해 수행됩니다.

| 구분 | 내용 |
| :--- | :--- |
| **관리 책임자 (Manager)** | **[본인 이름 또는 팀명 입력]** |
| **담당 파트** | OSS 저작권 및 라이선스 검토 (OSS Copyright & License Compliance) |
| **문의처 (Contact)** | [이메일 주소 또는 GitHub 프로필 링크] |
| **업데이트 기준** | 신규 라이브러리 추가, 버전 변경, 또는 의존성(Dependency) 변경 시 즉시 갱신 |
| **데이터 원본** | `/oss-compliance/manifest/MANIFEST.json` |

## 1.3 Internal OSS Policy Summary (내부 OSS 정책 요약)

`vacuum-cleaner` 프로젝트팀은 법적 분쟁을 예방하고 코드의 안정성을 확보하기 위해, 별도의 내부 정책서(`OSS-POLICY.md`)에 의거하여 다음과 같은 **라이선스 허용 기준**을 엄격히 적용하고 있습니다.

### A. 라이선스 분류 기준 (License Classification)

| 등급 | 상태 | 라이선스 유형 | 정책 및 조치 사항 |
| :--- | :--- | :--- | :--- |
| **Green** | **허용 (Allowed)** | MIT, Apache-2.0, BSD-3-Clause, ISC | - 자유롭게 사용 가능<br>- **의무:** 저작권 고지 및 라이선스 전문 포함 (`NOTICE` 반영) |
| **Yellow** | **주의 (Caution)** | LGPL, MPL, EPL | - 사용 시 담당자 검토 필수<br>- **의무:** 소스 코드 수정 시 해당 파일 공개, 반드시 동적 링크(Dynamic Linking) 사용 |
| **Red** | **금지 (Prohibited)** | GPLv2/v3, AGPL, CPOL | - **사용 엄격 금지**<br>- 사유: 전염성(Viral Effect)으로 인해 프로젝트 전체 소스 코드 공개 의무 발생 |

### B. 사용 승인 절차 (Approval Workflow)

모든 개발 팀원은 새로운 외부 라이브러리를 도입하기 전, 반드시 **사전 승인 절차**를 거쳤습니다.

1.  **식별(Identification):** 라이브러리의 라이선스 유형 확인 (Green/Red 여부 판별).
2.  **검토(Review):** 저작권 관리 책임자에게 사용 목적과 라이선스 정보를 제출.
3.  **승인 및 기록(Approval & Record):** 책임자 승인 후 `MANIFEST.json`에 등록하고 소스 코드에 반영.

> **Note:** 본 보고서의 **Section 2**에 나열된 모든 OSS는 위 정책에 따라 **'Green' 등급**으로 판별되었거나, 적법한 절차를 거쳐 승인된 소프트웨어임을 확인합니다.
