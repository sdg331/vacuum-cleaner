# 대표적 OSS 소개 - 장주연

오픈소스 소프트웨어(Open Source Software, OSS)는 소스 코드가 공개되어 누구나 열람·수정·재배포할 수 있도록 허용되는 소프트웨어를 의미한다.  
이는 단순히 무료 사용 여부를 넘어, 라이선스 조건에 따라 사용·연구·수정·배포의 자유를 부여하는 개발·배포 방식이다.

본 문서는 여러 분야에서 널리 사용되는 대표적인 OSS 프로젝트를 선정하여,  
각 프로젝트의 역할과 함께 사용 허용 범위, 재배포 조건 등 라이선스 특성을 정리한다.

---

## 목차

1. 분야별 대표 OSS 요약 표  
2. 운영체제 / 플랫폼  
3. 데이터베이스  
4. 웹 서버 / 런타임  
5. 개발 언어 / 런타임  
6. 개발 도구 / 협업 도구  
7. 참고 문헌 / 출처  

---

## 1. 분야별 대표 OSS 요약 표

| 분야                 | 프로젝트              | 주요 역할/특징                                             | 대표 사용 목적                              | 라이선스 요약                                      |
|----------------------|-----------------------|-------------------------------------------------------------|---------------------------------------------|----------------------------------------------------|
| 운영체제 / 플랫폼    | Linux 커널            | 리눅스 계열 OS의 핵심 커널                                 | 범용 OS 커널, 임베디드·서버 기반           | GPLv2-only                                        |
| 운영체제 / 플랫폼    | Android (AOSP)        | 안드로이드 플랫폼의 공개 소스 코드 베이스                  | 모바일 OS 플랫폼 개발                       | Apache 2.0 (주요 구성요소)                        |
| 운영체제 / 플랫폼    | FreeBSD               | BSD 계열 유닉스 운영체제                                   | 서버, 네트워크·스토리지용 OS               | BSD 2-Clause (FreeBSD License)                    |
| 데이터베이스         | PostgreSQL            | 범용 관계형 데이터베이스 관리 시스템(RDBMS)                | 일반 업무용·서비스용 DB                     | PostgreSQL License (BSD 계열, 관대함)             |
| 데이터베이스         | MySQL Community       | 대표적인 오픈소스 RDBMS                                    | 웹 서비스용 DB                              | GPLv2 (커뮤니티 버전)                             |
| 데이터베이스         | MongoDB Community     | 도큐먼트 지향 NoSQL 데이터베이스                           | 문서·이벤트 데이터 저장                     | SSPL-1.0 (강한 copyleft, OSI 비승인)              |
| 웹 서버 / 런타임     | Apache HTTP Server    | 모듈형 HTTP 웹 서버                                        | 웹 서버, 리버스 프록시                      | Apache License 2.0                                |
| 웹 서버 / 런타임     | Nginx                 | 이벤트 기반 경량 웹 서버 및 리버스 프록시                  | 정적 서빙, 프록시, 로드 밸런서             | BSD 2-Clause                                      |
| 웹 서버 / 런타임     | Node.js               | 서버 측 JavaScript 실행 환경                               | API 서버, 백엔드 런타임                    | MIT License                                       |
| 개발 언어 / 런타임   | Python                | 범용 고수준 프로그래밍 언어                                | 스크립트, 데이터·웹 애플리케이션           | PSF License (BSD 스타일, GPL 호환)               |
| 개발 언어 / 런타임   | Rust                  | 메모리 안전성을 목표로 한 시스템 프로그래밍 언어           | 시스템 도구, 저수준 라이브러리              | 듀얼 라이선스: Apache 2.0 / MIT                   |
| 개발 언어 / 런타임   | OpenJDK (Java)        | Java 언어와 JVM의 참조 구현                                | Java 기반 애플리케이션 실행 환경           | GPLv2 + Classpath Exception                       |
| 개발 도구 / 협업 도구 | Git                  | 분산 버전 관리 도구                                        | 소스 코드 변경 이력 관리                    | GPLv2-only                                        |
| 개발 도구 / 협업 도구 | Docker Engine (Moby) | 컨테이너 실행 엔진                                         | 컨테이너 기반 애플리케이션 실행            | Apache License 2.0                                |
| 개발 도구 / 협업 도구 | VS Code (Code - OSS) | 확장 가능한 소스 코드 에디터                               | 일반 개발용 에디터                          | MIT License (소스, Code - OSS)                   |

---

## 2. 운영체제 / 플랫폼

### 2.1 Linux 커널 (Linux Kernel)

Linux 커널은 일반적인 리눅스 운영체제 배포판과 안드로이드 등 다양한 시스템의 핵심이 되는 커널이다.  
프로세스 관리, 메모리 관리, 파일 시스템, 네트워크 스택, 장치 드라이버 등 운영체제의 기반 기능을 제공한다.

Linux 커널은 전체적으로 GNU GPLv2-only 라이선스를 따른다. 커널 문서에서 커널 전체가 GPLv2로 라이선스된다고 명시되어 있으며, GPLv3가 아닌 GPLv2에 고정되어 있다. GPLv2는 강한 copyleft 라이선스로, 커널을 수정하여 배포하는 경우 해당 수정 부분의 소스 코드 공개가 요구된다.  
커널 소스는 공개 저장소를 통해 관리되며, 전 세계 개발자가 패치를 제출하고 공개적으로 코드 리뷰가 이루어지는 방식으로 개발이 진행된다.

---

### 2.2 Android Open Source Project (AOSP)

Android Open Source Project(AOSP)는 안드로이드 운영체제를 구성하는 공개 소스 코드 집합이다.  
플랫폼 프레임워크, 시스템 서비스, 기본 라이브러리, 기본 앱 등 안드로이드 시스템의 핵심 요소가 포함된다.

AOSP의 주요 구성 요소는 Apache License 2.0 아래 배포된다. Apache 2.0은 소스 코드 수정·재배포를 허용하면서도, 수정된 소스를 공개할 의무를 강제하지 않는 관대한(permissive) 라이선스이다. 일부 구성 요소는 GPL 또는 LGPL을 사용하지만, 전체 플랫폼은 Apache 2.0 위주로 설계되어 있다.  
AOSP 소스 코드는 누구나 내려받아 빌드·수정할 수 있으며, 제조사나 커뮤니티는 이를 기반으로 자체 안드로이드 변형판을 제작할 수 있다.

---

### 2.3 FreeBSD

FreeBSD는 BSD 계열 유닉스 운영체제로, 서버·네트워크·스토리지용 운영체제로 활용되는 범용 OS이다.  
네트워크 스택과 파일 시스템, 안정성 등이 강점으로 알려져 있다.

FreeBSD는 BSD 2-Clause 라이선스를 사용한다. 이 라이선스는 저작권 표시와 면책 조항을 유지하는 조건 아래, 소프트웨어의 사용·수정·재배포를 폭넓게 허용한다. 수정된 소스를 공개할 의무가 없으므로, 상용 제품에 코드 일부를 포함하는 것도 가능하다.  
프로젝트는 커미터 제도와 코어 팀에 의해 관리되며, 모든 소스 변경은 공개 저장소와 코드 리뷰 과정을 거쳐 반영된다.

---

## 3. 데이터베이스

### 3.1 PostgreSQL

PostgreSQL은 범용 관계형 데이터베이스 관리 시스템(RDBMS)으로, 트랜잭션 처리, 표준 SQL, 다양한 인덱스와 확장 기능을 제공한다. 일반적인 업무용 애플리케이션과 서비스에서 데이터 저장·조회용 DB로 사용할 수 있다.

PostgreSQL은 PostgreSQL License를 사용한다. 이는 BSD·MIT 계열과 유사한 관대한 라이선스로, 소스 코드를 수정하여 상용 제품에 포함하더라도 소스 공개 의무가 없다. 단, 저작권과 라이선스 고지는 유지해야 한다.  
프로젝트는 특정 기업 소유가 아닌 커뮤니티 주도 방식으로 운영되며, 개발자·기업·사용자 그룹이 메일링 리스트와 회의를 통해 기능 추가와 변경을 논의한다.

---

### 3.2 MySQL Community Edition

MySQL은 관계형 데이터베이스 관리 시스템으로, 웹 애플리케이션과 일반 서비스에서 데이터 저장용으로 널리 사용된다. SQL 기반 질의, 테이블·인덱스 관리, 트랜잭션 기능 등을 제공한다.

MySQL Community Edition은 GNU GPLv2 라이선스를 따른다. GPLv2는 소프트웨어를 수정·배포할 수 있도록 허용하지만, 배포 시 파생 저작물의 소스를 GPL 조건에 따라 공개해야 한다. 이에 따라 애플리케이션과 함께 MySQL을 번들링하여 배포하는 경우, 라이선스 조건을 검토할 필요가 있다.  
MySQL은 별도의 상용 라이선스를 통해 비공개 코드와 함께 사용하는 모델도 제공하며, 이 때문에 “커뮤니티(GPL) + 상용” 구조의 듀얼 라이선스를 사용하는 대표적인 DB 프로젝트로 분류된다.

---

### 3.3 MongoDB Community Server

MongoDB는 JSON/BSON 형식의 문서를 저장하는 도큐먼트 지향 NoSQL 데이터베이스이다. 스키마가 고정되지 않으며, 문서 단위로 데이터를 관리한다.

MongoDB Community Server는 Server Side Public License(SSPL)를 사용한다. SSPL은 MongoDB에서 정의한 라이선스로, 소스를 공개하고 수정·사용할 수 있도록 허용하지만, 데이터베이스를 서비스 형태로 제공하는 경우 서비스 전체 스택에 대한 소스 공개를 요구하는 조항을 포함한다.  
이러한 이유로 SSPL은 OSI에서 승인한 오픈소스 라이선스로 분류되지 않으며, 일반적인 오픈소스 라이선스와는 구별되는 특성이 있다. 소스 코드는 공개되어 있으나, 서버·서비스 환경에서 사용 시 라이선스 조항을 상세히 검토할 필요가 있다.

---

## 4. 웹 서버 / 런타임

### 4.1 Apache HTTP Server

Apache HTTP Server는 HTTP 프로토콜을 사용하는 웹 서버 소프트웨어로, 정적·동적 웹 콘텐츠 제공을 위한 서버로 사용된다. 모듈 구조를 통해 SSL, URL 재작성, 인증, 스크립트 연동 등 여러 기능을 확장할 수 있다.

Apache HTTP Server는 Apache License 2.0으로 배포된다. Apache 2.0은 소프트웨어의 사용·수정·재배포를 허용하며, 특허권 관련 조항을 명확히 포함한다. 수정된 버전을 배포하더라도 소스 공개 의무는 없으며, 라이선스 및 저작권 표시 유지가 요구된다.  
프로젝트는 Apache Software Foundation 산하에서 관리되며, 프로젝트 관리 위원회와 커미터에 의해 개발과 릴리스가 진행된다.

---

### 4.2 Nginx

Nginx는 HTTP 웹 서버이자 리버스 프록시 서버로, 이벤트 기반 처리 모델을 사용하여 동시 접속 처리를 수행한다. 정적 파일 제공, 백엔드 서버로의 프록시, 로드 밸런싱, SSL 종료 등의 용도로 사용된다.

Nginx의 오픈소스 버전은 BSD 2-Clause 라이선스를 사용한다. 이 라이선스는 소스 코드의 수정·재배포를 허용하고, 수정본을 상용 제품에 포함시키는 것도 제한하지 않는다. 소스 공개 의무는 없으며, 저작권 및 면책 조항을 유지해야 한다.  
공개된 소스는 누구나 내려받아 빌드할 수 있으며, 설정 파일을 통해 동작 방식을 세부 조정할 수 있다.

---

### 4.3 Node.js

Node.js는 JavaScript를 서버 측에서 실행할 수 있도록 하는 런타임 환경이다. 비동기 I/O와 이벤트 루프 기반 구조를 제공하여, 네트워크 애플리케이션과 API 서버 작성에 사용된다.

Node.js는 MIT License로 배포된다. MIT 라이선스는 소프트웨어의 사용·복사·수정·재배포를 폭넓게 허용하며, 소스 공개 의무가 없다. 저작권 및 허가 고지만 유지하면 상용·비상용 소프트웨어 어디에나 포함할 수 있다.  
Node.js 개발은 공개 저장소와 이슈 트래커를 통해 진행되며, 제안 문서와 코드 리뷰 과정을 거쳐 기능이 추가된다.

---

## 5. 개발 언어 / 런타임

### 5.1 Python

Python은 범용 고수준 프로그래밍 언어로, 스크립트 작성, 웹 애플리케이션, 데이터 처리, 자동화 등 다양한 용도에 사용된다. CPython은 Python 언어의 대표 구현체로, 인터프리터와 표준 라이브러리를 포함한다.

Python은 Python Software Foundation License(PSFL)를 사용한다. PSFL은 BSD 스타일의 관대한 라이선스로 분류되며, Python 인터프리터를 수정·재배포할 수 있도록 허용한다. Python을 사용한 애플리케이션은 소스 공개 의무 없이 상용 배포가 가능하며, 저작권 및 라이선스 고지는 유지해야 한다.  
언어 기능 추가와 변경은 PEP(Python Enhancement Proposal) 문서를 통해 공개적으로 제안·논의된다.

---

### 5.2 Rust

Rust는 메모리 안전성과 성능을 함께 고려한 시스템 프로그래밍 언어이다. 소유권, 빌림, 라이프타임 등의 개념을 사용해 컴파일 시점에 메모리 오류를 검출하도록 설계되어 있다.

Rust 프로젝트는 Apache License 2.0과 MIT License의 듀얼 라이선스를 채택하고 있다. 사용자는 두 라이선스 중 하나를 선택해 이용할 수 있으며, 두 라이선스 모두 관대한(permissive) 라이선스에 속한다. 이를 통해 Rust 컴파일러와 표준 라이브러리는 상용·비상용 소프트웨어에 폭넓게 포함될 수 있다.  
언어와 표준 라이브러리의 소스 코드는 공개 저장소에서 관리되며, RFC와 코드 리뷰를 통해 기능이 발전한다.

---

### 5.3 OpenJDK (Java)

OpenJDK는 Java 언어와 JVM(Java Virtual Machine)의 오픈소스 참조 구현이다. Java 컴파일러, 표준 클래스 라이브러리, 가상 머신 등이 포함되어 있으며, 여러 JDK 배포판의 기반이 된다.

OpenJDK는 GNU GPLv2와 Classpath Exception 조합으로 라이선스된다. GPLv2는 소스 공개를 요구하는 copyleft 라이선스지만, Classpath Exception은 OpenJDK 위에서 실행되는 애플리케이션의 코드가 GPL의 전염 대상이 되지 않도록 예외를 둔다.  
이를 통해 런타임과 표준 라이브러리는 공개된 상태로 유지되면서, 일반 Java 애플리케이션은 별도의 라이선스를 가지고 배포될 수 있다.

---

## 6. 개발 도구 / 협업 도구

### 6.1 Git

Git은 분산 버전 관리 시스템으로, 소스 코드 변경 이력을 관리하고 브랜치·머지 기능을 제공한다. 로컬 저장소와 원격 저장소를 함께 사용하여, 여러 개발자가 동시에 작업할 수 있도록 지원한다.

Git은 GNU GPLv2 라이선스를 따른다. 이 라이선스는 소프트웨어의 수정·재배포를 허용하지만, 수정본을 배포하는 경우 해당 소스 코드를 GPL 조건에 따라 공개해야 한다.  
일반 사용자는 Git 바이너리를 설치하여 사용하는 수준이므로, 도구 사용 자체에는 추가 의무가 없으며, 프로젝트 개발은 공개 저장소와 메일링 리스트를 통해 이루어진다.

---

### 6.2 Docker Engine / Moby

Docker는 컨테이너 기술을 통해 애플리케이션과 실행 환경을 이미지로 패키징하고, 이를 컨테이너로 실행할 수 있도록 하는 도구이다. Docker Engine의 오픈소스 기반은 Moby 프로젝트로 분리되어 있다.

Moby/Docker Engine은 Apache License 2.0으로 배포된다. Apache 2.0은 소스 수정·재배포와 상용 사용을 허용하며, 특허 관련 조항을 명시한다. 수정된 버전을 배포하더라도 소스 공개 의무는 없고, 저작권·라이선스 고지 유지가 요구된다.  
컨테이너 엔진 소스 코드는 공개 저장소에 존재하며, 누구나 빌드·실행·기여할 수 있다.

---

### 6.3 Visual Studio Code (Code - OSS)

Visual Studio Code(VS Code)는 소스 코드 편집, 디버깅, 확장 설치 등을 지원하는 코드 에디터이다. 다양한 언어와 도구를 확장(Extension) 형태로 추가할 수 있으며, Git 연동 기능이 기본 제공된다.

VS Code의 오픈소스 코드베이스는 GitHub의 `microsoft/vscode` 리포지토리(Code - OSS)에 공개되어 있으며, MIT License로 배포된다. MIT 라이선스는 소프트웨어 사용·복사·수정·재배포를 폭넓게 허용하며, 소스 공개 의무가 없다.  
공개된 코드베이스를 기반으로, 텔레메트리 및 상표를 제거한 포크 버전 등도 제작되어 배포되고 있다.

---

## 7. 참고 문헌 / 출처

### 7.1 Linux 커널 라이선스

- Linux kernel documentation – “Linux kernel licensing rules”, docs.kernel.org  

### 7.2 Android / AOSP 라이선스

- Android Open Source Project – “Content license”, source.android.com  
- Android Open Source Project – “Contributor license agreements and headers”, source.android.com  

### 7.3 FreeBSD 및 BSD 라이선스

- The FreeBSD Project – “Licensing”, freebsd.org  

### 7.4 PostgreSQL 라이선스

- PostgreSQL Global Development Group – “PostgreSQL: License”, postgresql.org  
- PostgreSQL Global Development Group – “PostgreSQL Press FAQ”, postgresql.org  
- 한국 공개SW 포털(OLIS) – PostgreSQL 라이선스 관련 설명  

### 7.5 MySQL / 듀얼 라이선스

- Oracle MySQL – MySQL Community Edition 및 Licensing 관련 문서  

### 7.6 MongoDB / SSPL 관련

- MongoDB Inc. – “Server Side Public License FAQ”, mongodb.com  
- “Server Side Public License” 관련 문서 및 OSI 관련 자료  
- The New Stack – “The Case Against the Server Side Public License (SSPL)”  

### 7.7 Apache HTTP Server / Apache License 2.0

- Apache Software Foundation – “Apache License, Version 2.0”  
- Apache HTTP Server Project 페이지  

### 7.8 기타 언어·런타임 및 도구

- Python Software Foundation – PSF License 및 Python.org 라이선스 페이지  
- Rust Project / Rust Foundation – Rust 언어 라이선스 안내 문서  
- OpenJDK – “GPLv2 with the Classpath Exception” 관련 문서 및 FAQ  
- Git – git-scm.com 및 GNU GPLv2 라이선스 전문  
- Moby / Docker Engine – GitHub 및 Docker 공식 문서  
- Visual Studio Code – GitHub `microsoft/vscode` (Code - OSS) 리포지토리 및 MIT License  
- GNU Project – “GNU General Public License v2.0”, gnu.org  
