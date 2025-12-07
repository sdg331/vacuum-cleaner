```markdown
#  소스코드 라이선스 헤더(Header) 적용 가이드

이 문서는 개발자가 새로운 소스코드 파일을 생성할 때, 파일 최상단에 포함해야 하는 **라이선스 고지문(License Header)**의 표준 양식을 제공합니다.

> ** 왜 헤더를 붙여야 하나요?**
>
> `LICENSE` 파일이 프로젝트 루트에 있어도, 코드가 개별 파일 단위로 복사되어 인터넷에 돌아다닐 수 있습니다.
> 파일 내부에 헤더가 없으면 저작권 보호를 받기 어렵거나, 제3자가 무단으로 도용할 위험이 커집니다.

---

## 1.  작성 원칙 (Common Rules)
1. **위치:** 반드시 파일의 **가장 첫 줄**(Shebang `#!/bin/bash` 등이 있다면 그 바로 아래)에 위치해야 합니다.
2. **수정 금지:** 오픈소스 코드를 가져왔을 때, 원작자의 헤더를 **절대로 삭제하면 안 됩니다.**
3. **추가 작성:** 원본 코드를 수정했다면, 원작자 헤더 아래에 `Modified by [Your Name]` 형태의 주석을 추가합니다.
4. **Placeholder:** 아래 예시에서 `[yyyy]`, `[name of copyright owner]` 부분은 본인의 정보로 변경해서 사용하세요.

---

## 2. 라이선스별 / 언어별 템플릿 (Copy & Paste)

### Type A: MIT License (가장 많이 사용)
짧고 간결합니다. Python, Node.js 프로젝트에서 주로 쓰입니다.

#### [Python / Ruby / Shell]
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
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND...
```

#### [JavaScript / TypeScript / C / C++ / Java / Swift]
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
 */
```

---

### Type B: Apache License 2.0 (기업용/안드로이드)
Google, Spring, Hadoop 등 대형 프로젝트 표준입니다. 특허 조항이 포함되어 있습니다.

#### [Java / C / C++ / Kotlin]
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

#### [XML / HTML]
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

### Type C: GNU GPL v3 (강력한 소스 공개 의무)
가장 엄격합니다. 사용자가 이 코드를 봤을 때 "아, 이건 함부로 쓰면 안 되겠구나"라고 바로 알 수 있게 해야 합니다.

#### [C / C++ / General]
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

## 3. 최신 트렌드: SPDX 식별자 (Short Form)
최근 리눅스 커널(Linux Kernel) 등에서는 긴 헤더 대신 **SPDX ID** 한 줄만 적어서 파일 용량을 줄이고 가독성을 높이기도 합니다.

**사용법:** 파일 첫 줄에 아래와 같이 주석으로 명시

```
# SPDX-License-Identifier: MIT
```

```
// SPDX-License-Identifier: Apache-2.0
```

```
/* SPDX-License-Identifier: GPL-3.0-or-later */
```

> **Note:** SPDX 방식을 사용하더라도 프로젝트 최상위 루트에는 반드시 전체 텍스트가 담긴 `LICENSE` 파일이 존재해야 합니다.
```
