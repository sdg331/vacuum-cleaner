```markdown
# 🛡️ 소스코드 라이선스 헤더(Header) 적용 가이드

> **이 문서는 개발자를 위한 실무 가이드입니다.**
>
> 새로운 소스코드 파일을 생성할 때, 파일 최상단에 포함해야 하는 **라이선스 고지문(License Header)**의 표준 양식을 제공합니다. 이를 통해 코드의 법적 보호를 강화하고 오픈소스 컴플라이언스를 준수할 수 있습니다.

---

## ❓ 왜 파일마다 헤더를 붙여야 하나요?

`LICENSE` 파일이 프로젝트 루트(Root)에 있어도, **코드가 개별 파일 단위로 복사되어 배포**될 경우 법적 보호를 받기 어렵습니다.

1.  **저작권 보호:** 파일 자체가 독립적으로 배포되더라도 저작권자가 누구인지 명확히 알립니다.
2.  **무단 도용 방지:** 제3자가 코드를 사용할 때 준수해야 할 의무를 즉시 확인할 수 있습니다.
3.  **컴플라이언스:** 많은 오픈소스 라이선스(Apache, GPL 등)는 파일 내 고지를 권장하거나 의무화합니다.

---

## 1. 📌 작성 원칙 (Common Rules)

반드시 아래 규칙을 준수하여 헤더를 작성하세요.

*   **위치 준수:** 파일의 **가장 첫 줄**에 위치해야 합니다. (단, `#!/bin/bash` 같은 Shebang이 있다면 그 바로 아래)
*   **삭제 금지:** 외부 오픈소스 코드를 가져왔을 때, **원작자의 헤더를 절대로 삭제하지 마십시오.**
*   **수정 이력:** 원본 코드를 수정했다면, 원작자 헤더 아래에 `Modified by [Your Name]` 형태의 주석을 추가합니다.
*   **치환(Placeholder):** 아래 템플릿의 `[yyyy]`(연도)와 `[name of copyright owner]`(이름/회사명)를 본인의 정보로 변경하세요.

---

## 2. 📝 라이선스별 템플릿 (Copy & Paste)

가장 널리 사용되는 3가지 라이선스(MIT, Apache, GPL)의 표준 헤더입니다.

### 🔹 Type A: MIT License
> **특징:** 가장 짧고 간결하며, 제약이 적습니다. (Python, Node.js 생태계 표준)

#### 🐍 Python / Ruby / Shell
```
# Copyright (c) [yyyy] [name of copyright owner]
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
```

#### ☕ JavaScript / C / Java / Swift
```
/*
 * Copyright (c) [yyyy] [name of copyright owner]
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND... (이하 생략 가능하나 전체 권장)
 */
```

---

### 🔹 Type B: Apache License 2.0
> **특징:** 특허 조항이 포함되어 기업용 프로젝트 및 Android 생태계에서 선호합니다.

#### ☕ Java / C / Kotlin
```
/*
 * Copyright [yyyy] [name of copyright owner]
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
```

#### 🌐 XML / HTML
```
<!--
  Copyright [yyyy] [name of copyright owner]

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
```

---

### 🔹 Type C: GNU GPL v3
> **특징:** 가장 강력한 **Copyleft(전염성)**를 가집니다. 소스 공개 의무를 강력히 경고합니다.

#### 🖥️ C / C++ / General
```
/*
 * This file is part of [Program Name].
 *
 * Copyright (C) [yyyy] [name of copyright owner]
 *
 * [Program Name] is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * [Program Name] is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */
```

---

## 3. 🚀 최신 트렌드: SPDX 식별자 (Short Form)

최근 Linux Kernel 등 대형 프로젝트에서는 파일 용량 절약과 자동화 도구의 인식을 돕기 위해 **SPDX ID**를 사용합니다.

*   **장점:** 코드가 깔끔해지고 가독성이 좋아집니다.
*   **주의:** 반드시 프로젝트 루트에 전체 텍스트가 담긴 `LICENSE` 파일이 존재해야 유효합니다.

#### 사용 예시

**Python / Shell**
```
# SPDX-License-Identifier: MIT
```

**Java / C / JS**
```
// SPDX-License-Identifier: Apache-2.0
```

**C (Block Comment)**
```
// SPDX-License-Identifier: GPL-3.0-or-later //
```
