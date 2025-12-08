# 대표적 OSS 소개 - 장주연

오픈소스 소프트웨어(Open Source Software, OSS)는 소스 코드가 공개되어 누구나 열람·수정·재배포할 수 있도록 허용하는 소프트웨어를 의미한다. 이는 단순히 소프트웨어를 무료로 사용할 수 있다는 의미를 넘어, 라이선스가 보장하는 권한에 따라 사용(Use), 연구(Study), 수정(Modify), 재배포(Distribute)의 자유를 제공하는 개발 및 배포 방식이다. 이러한 공개성은 개발자 간 협업을 촉진하고, 소프트웨어의 투명성·보안성·지속적인 개선 가능성을 높이는 중요한 기반이 된다.

현대의 소프트웨어 생태계에서 OSS는 운영체제, 데이터베이스, 프로그래밍 언어, 개발 도구, 클라우드 플랫폼 등 다양한 분야의 핵심 구성 요소로 자리 잡고 있다. 기업과 개인 개발자는 OSS를 직접 활용하거나, 이를 기반으로 새로운 서비스를 구축하는 방식으로 생태계를 확장하고 있다.

본 문서는 여러 기술 분야에서 널리 사용되는 대표적인 오픈소스 프로젝트들을 선정하여,
각 프로젝트의 기능적 역할, 적용 분야, 사용 시 요구되는 라이선스 조건, 수정·재배포 시 준수해야 하는 의무사항 등을 체계적으로 정리한다. 특히 GPL, LGPL, MIT, Apache License 등 주요 오픈소스 라이선스 간의 사용 허용 범위 차이, Copyleft 적용 여부, 상업적 이용 가능성 등의 관점에서 비교·분석함으로써, OSS 활용 시 고려해야 하는 법적·기술적 요소들을 명확하게 이해하는 데 목적이 있다.

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

| 분야 | 프로젝트 | 간단한 설명 | 라이선스 |
|------|----------|--------------|----------|
| 운영체제 / 플랫폼 | Linux 커널 | 리눅스 계열 운영체제의 핵심 커널로 프로세스, 메모리, 파일 시스템, 네트워크 기능을 담당 | GPLv2-only |
|  | Android (AOSP) | 안드로이드 운영체제를 구성하는 공개 소스 코드 기반 | Apache 2.0 |
|  | FreeBSD | BSD 계열 유닉스 운영체제로 서버·네트워크용 OS로 사용 | BSD 2-Clause |
| 데이터베이스 | PostgreSQL | 표준 SQL을 지원하는 범용 관계형 데이터베이스 관리 시스템 | PostgreSQL License |
|  | MySQL Community | SQL 기반 오픈소스 관계형 데이터베이스 | GPLv2 |
|  | MongoDB Community | JSON/BSON 기반의 도큐먼트 지향 NoSQL 데이터베이스 | SSPL-1.0 |
| 웹 서버 / 런타임 | Apache HTTP Server | 모듈형 구조의 HTTP 웹 서버 소프트웨어 | Apache License 2.0 |
|  | Nginx | 이벤트 기반 웹 서버 및 리버스 프록시 서버 | BSD 2-Clause |
|  | Node.js | JavaScript를 서버 측에서 실행하는 런타임 환경 | MIT License |
| 개발 언어 / 런타임 | Python | 범용 고수준 인터프리터 프로그래밍 언어 | PSF License |
|  | Rust | 메모리 안전성을 중시하는 시스템 프로그래밍 언어 | Apache 2.0 / MIT |
|  | OpenJDK (Java) | Java 언어와 JVM의 오픈소스 참조 구현 | GPLv2 + Classpath Exception |
| 개발 도구 / 협업 | Git | 분산 버전 관리 시스템 | GPLv2-only |
|  | Docker Engine (Moby) | 컨테이너 기반 애플리케이션 실행 엔진 | Apache License 2.0 |
|  | VS Code (Code - OSS) | 확장 가능한 오픈소스 코드 에디터 | MIT License |

---
## 2. 운영체제 / 플랫폼 (Operating Systems & Platforms)

### 2.1 Linux 커널 (Linux Kernel)

Linux 커널은 현대 컴퓨팅 환경에서 광범위하게 사용되는 운영체제 커널로, 서버·데스크톱·임베디드 시스템·IoT 기기·안드로이드 등 다양한 플랫폼의 핵심 요소로 활용된다. 커널은 하드웨어와 사용자 공간(User Space) 프로그램 사이에서 자원 관리 및 추상화를 제공하는 계층으로, 운영체제의 본질적인 기능을 담당한다.

#### 주요 기능

- **프로세스 관리(Process Scheduling)**  
  선점형 스케줄링 기반의 CFS(Completely Fair Scheduler)를 포함하며, 프로세스 생성·전환·종료 및 우선순위 관리 기능을 제공한다.

- **메모리 관리(Memory Management)**  
  가상 메모리 관리, 페이지 캐시, NUMA 구조 지원 등을 포함해 고성능 메모리 환경을 지원한다.

- **파일 시스템(File System)**  
  ext4, XFS, Btrfs, F2FS 등 다양한 파일 시스템을 탑재하며, VFS(Virtual File System) 계층을 통해 통일된 파일 접근 인터페이스를 제공한다.

- **네트워크 스택(Network Stack)**  
  TCP/IP 프로토콜 스택, Netfilter 방화벽, eBPF 기반 패킷 처리 기능 등을 포함한다.

- **장치 드라이버(Device Drivers)**  
  수천 종 이상의 하드웨어 장치를 지원하며, 커널 모듈 형태로 동적 로딩이 가능하다.

#### 라이선스

Linux 커널 전체는 **GNU GPLv2-only** 라이선스를 따른다.  
GPLv2는 강한 Copyleft 라이선스로 다음 의무를 포함한다.

- 커널 또는 커널 기반 파생물을 배포할 경우, 수정된 소스 코드 전체를 공개해야 함  
- GPLv3와의 호환성 문제로 인해 커널은 의도적으로 GPLv2에 고정됨  
- 사용자 공간 프로그램이 커널과 상호작용하는 것 자체는 GPLv2 전염에 해당되지 않음  
  *(시스템 호출 인터페이스는 라이선스 전염에서 제외)*

#### 개발 방식

- 전 세계 개발자가 Git 기반 저장소(Linus Torvalds의 리눅스 리포지토리)에 패치를 제출  
- 수십 명의 유지관리자(Maintainer)가 서브시스템을 관리하며, 코드 리뷰 후 머지  
- 릴리스는 약 8주 단위로 이루어지며, 장기지원(LTS) 버전도 별도로 존재  

---

### 2.2 Android Open Source Project (AOSP)

AOSP는 안드로이드 OS의 기본 구성요소를 포함한 대규모 오픈소스 프로젝트이다.  
구성 요소는 다음과 같은 계층을 포함한다.

#### 주요 구성

- 플랫폼 프레임워크: 안드로이드 API와 시스템 서비스 제공  
- 런타임 ART(Android Runtime): 바이트코드 실행 및 JIT/AOT 컴파일  
- 하드웨어 추상화 계층(HAL): OEM 제조사가 하드웨어를 구현하는 인터페이스  
- 기본 앱 및 시스템 UI 요소  
- 빌드 시스템(Soong, Make)

#### 라이선스

AOSP의 대부분은 **Apache License 2.0**을 따른다.

- 수정한 소스를 공개할 의무 없음  
- 특허권 관련 사용 허용 조항 포함  
- 상용 안드로이드 배포 시에도 라이선스 부담이 없음  
- 단, 일부 구성 요소(OS 핵심 라이브러리 등)는 GPL/LGPL을 포함하고 있어 OEM은 이를 준수해야 함  

#### 특징

- 누구나 소스를 내려받아 빌드하여 자체 OS 버전 제작 가능  
- OEM 제조사는 AOSP 기반에 자체 UI·앱·펌웨어를 추가하여 디바이스 제품화  
- 구글의 앱 및 서비스(GMS)는 AOSP와 별개의 라이선스·계약 구조로 제공됨  

---

### 2.3 FreeBSD

FreeBSD는 BSD 계열 운영체제로, 안정성, 성능, 네트워크 스택 품질이 높아 서버·스토리지·라우터 등에서 많이 사용된다.

#### 특징적 요소

- 고성능 TCP/IP 스택  
- 강력한 ZFS 파일 시스템 지원  
- Jail 기반 가벼운 컨테이너 격리 기능 제공  
- 높은 안정성과 긴 릴리스 지원 주기  

#### 라이선스

FreeBSD는 **BSD 2-Clause License**를 사용한다.

- 저작권 표시 및 면책 조항 유지 시 자유롭게 사용 가능  
- 수정본 소스 공개 의무 없음  
- 상용 제품에 FreeBSD 코드를 통합하는 것도 허용  

#### 개발 구조

- “커미터(committer)” 제도 기반  
- 기술적 의사결정은 Core Team에서 조율  
- 모든 패치는 공개 저장소에서 리뷰 후 반영  

---

## 3. 데이터베이스

### 3.1 PostgreSQL

PostgreSQL은 기능적으로 완성도가 매우 높은 오픈소스 RDBMS로,  
다음과 같은 고급 기능을 제공한다.

#### 기능

- 완전한 ACID 트랜잭션  
- 광범위한 인덱스(B-tree, Hash, GiST, SP-GiST, GIN 등)  
- 확장이 용이한 구조 (사용자가 타입·함수·인덱스 작성 가능)  
- 트리거·스토어드 프로시저·뷰 등 고급 SQL 기능  
- 파티셔닝 및 레플리케이션 기능 제공  

#### 라이선스

- **PostgreSQL License** 사용  
- MIT/BSD 계열의 permissive 라이선스  
- 소스 공개 없이 상용 제품에 포함 가능  
- 라이선스 고지 유지 의무만 있음  

#### 개발 방식

- 특정 기업 주도 아님 → 완전한 커뮤니티 중심  
- 기능 제안은 메일링 리스트를 통해 논의  
- 주요 기업(Apple, Microsoft, AWS 등)도 기능 기여에 참여  

---

### 3.2 MySQL Community Edition

MySQL은 웹 서비스, 일반 서버 환경에서 매우 널리 사용되는 RDBMS이다.

#### 주요 기능

- SQL 기반 데이터 질의 및 트랜잭션  
- MyISAM/InnoDB 엔진  
- 외래키, 인덱스, 복제 기능 제공  

#### 라이선스

MySQL Community Edition은 **GPLv2**로 제공된다.

- 수정·재배포 가능  
- 단, 파생 저작물 배포 시 소스 공개 의무 발생  
- 상용 환경에서는 Oracle이 제공하는 상업 라이선스를 통해 비공개 사용 가능  
- GPL + 상용 라이선스를 병행하는 **듀얼 라이선스 구조**의 대표 사례  

---

### 3.3 MongoDB Community Server

MongoDB는 문서(Document) 지향 NoSQL DB로,  
JSON/BSON 기반 스키마 유연성과 수평 확장성을 강조한다.

#### 주요 기능

- 문서 기반 데이터 모델  
- 인덱스, 샤딩, 복제 세트 형태의 고가용성 지원  
- 동적 스키마 구조  
- 대규모 데이터 처리에 적합  

#### 라이선스

MongoDB Community Server는 **SSPL(Server Side Public License)**을 사용한다.

- 소스 수정·재배포 가능  
- 서비스 형태로 제공할 경우 **서비스 전체 스택 공개 요구**  
- 이 조항 때문에 OSI(Open Source Initiative)는 SSPL을 오픈소스 라이선스로 인정하지 않음  
- AWS, Azure 등 주요 클라우드에서 공식 SSPL 기반 호스팅이 불가  

---

## 4. 웹 서버 / 런타임

### 4.1 Apache HTTP Server

Apache HTTP Server는 전 세계적으로 가장 오래되고 안정적인 웹 서버 중 하나로,  
모듈 구조를 통해 다양한 기능을 확장할 수 있다.

#### 기능

- HTTP/HTTPS 요청 처리  
- CGI, PHP, Python 등 스크립트 연동  
- `mod_rewrite`를 통한 URL 라우팅  
- 인증 및 접근 제어 기능  
- 가상호스팅 지원  

#### 라이선스

- **Apache License 2.0**  
- 수정한 소스의 공개 의무 없음  
- 상용 제품 포함 가능  
- 특허 사용권에 대한 명시적 허가 조항 존재  

---

### 4.2 Nginx

Nginx는 이벤트 기반 아키텍처를 채택하여 매우 높은 동시성을 제공하는 웹 서버이다.

#### 주요 특징

- 비동기 이벤트 처리 모델  
- 정적 파일 처리 성능 우수  
- 리버스 프록시 및 로드밸런서로 널리 사용  
- SSL/TLS 처리 가능  

#### 라이선스

- **BSD 2-Clause License**  
- 매우 관대한 라이선스  
- 수정본을 상용 제품에 포함 가능  
- 소스 공개 의무 없음  

---

### 4.3 Node.js

Node.js는 서버 측 JavaScript 런타임으로, 이벤트 루프 기반 비동기 I/O 모델을 제공한다.

#### 특징

- 단일 스레드 기반 이벤트 루프  
- 고성능 네트워크 서버 개발에 적합  
- NPM 생태계를 통한 수십만 개의 패키지 활용 가능  

#### 라이선스

- **MIT License**  
- 상용 배포 및 재배포 매우 자유로움  
- 저작권 및 허가 고지 유지 필요  

---

## 5. 개발 언어 / 런타임

### 5.1 Python

Python은 범용 고수준 언어로, 다음과 같은 분야에서 폭넓게 사용된다.

- 데이터 분석, 머신러닝  
- 웹 개발(Django, Flask)  
- 자동화 스크립트  
- 시스템 관리  

#### 라이선스

- **PSFL(Python Software Foundation License)**  
- BSD 계열의 관대한 라이선스  
- Python 수정·재배포 가능  
- Python 기반 애플리케이션은 소스 공개 의무 없음  

---

### 5.2 Rust

Rust는 안전성과 성능을 모두 중요시하는 시스템 프로그래밍 언어이다.

#### 주요 특징

- 메모리 안전성(Null·Dangling Pointer 방지)  
- 소유권/빌림 모델을 통한 컴파일 시점 오류 검출  
- C/C++ 대체 언어로 주목  

#### 라이선스

- **MIT + Apache License 2.0 듀얼 라이선스**  
- 사용자는 둘 중 하나를 선택  
- 상업적 활용이 매우 용이  

---

### 5.3 OpenJDK (Java)

OpenJDK는 공식 Java 플랫폼의 오픈소스 구현체이다.

#### 주요 구성

- Java 컴파일러(javac)  
- 표준 라이브러리  
- HotSpot JVM  

#### 라이선스

- **GPLv2 + Classpath Exception**  
- 애플리케이션 개발 시 GPL 전염 방지  
- JVM과 표준 라이브러리 수정 시 GPLv2 공개 의무 적용  

---

## 6. 개발 도구 / 협업 도구

### 6.1 Git

Git은 분산 버전 관리 시스템(DVCS)으로, 협업 개발의 사실상 표준이다.

#### 기능

- 커밋 기반 이력 관리  
- 브랜치/머지를 통한 병렬 개발  
- 원격 저장소(Push/Pull) 기반 협업  
- 충돌 해결, 태그, 서브모듈 등 다양한 기능 제공  

#### 라이선스

- **GNU GPLv2**  
- Git 자체를 수정·배포할 경우 소스 공개 필요  
- 단순 사용자에게는 의무 없음  

---

### 6.2 Docker Engine / Moby

Docker는 컨테이너 기술을 활용하여 애플리케이션과 환경을 분리·포장하는 도구이다.

#### 핵심 기능

- 이미지 생성(Dockerfile)  
- 컨테이너 실행·관리  
- 레이어 기반 스토리지 구조  
- 네트워크·볼륨 관리  

#### 라이선스

- **Apache License 2.0**  
- 상업적 사용 가능  
- 소스 공개 의무 없음  

---

### 6.3 Visual Studio Code (Code - OSS)

VS Code는 Microsoft가 개발한 오픈소스 기반 코드 에디터이다.

#### 기능

- 코드 자동 완성  
- 디버깅 지원  
- 확장(Extension) 기반 기능 추가  
- Git 연동 기능 기본 제공  

#### 라이선스

- **MIT License**  
- 사용·수정·재배포 자유  
- Code - OSS 기반 포크 다수 존재


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
