# Python Docstring 섹션 형식 정리 (Google Style 기준)

Python에서 함수, 클래스, 모듈 등에 문서화를 위해 사용하는 **docstring**은 일정한 형식으로 작성하면 가독성과 유지보수성이 좋아집니다. 여기서는 **Google 스타일 Docstring**의 주요 섹션 형식과 그 의미를 정리합니다.

---

## 1. Args

### ✅ 의미

- 함수의 \*\*매개변수(parameter)\*\*를 설명하는 섹션입니다.
- 각 인자의 **이름, 자료형, 설명**을 포함합니다.

### ✅ 예시

```python
Args:
    name (str): 사용자 이름.
    age (int): 사용자 나이.
```

---

## 2. Returns

### ✅ 의미

- 함수의 **반환값**에 대해 설명합니다.
- 반환되는 자료형과 그 의미를 명시합니다.

### ✅ 예시

```python
Returns:
    bool: 로그인 성공 여부.
```

---

## 3. Raises

### ✅ 의미

- 함수 실행 중 발생할 수 있는 \*\*예외(exception)\*\*를 설명합니다.
- 예외 타입과 발생 조건을 명시합니다.

### ✅ 예시

```python
Raises:
    ValueError: 입력 값이 유효하지 않은 경우.
    ZeroDivisionError: 0으로 나눌 때.
```

---

## 4. Attributes (클래스에서 사용)

### ✅ 의미

- 클래스의 인스턴스 \*\*속성(attribute)\*\*을 설명할 때 사용합니다.

### ✅ 예시

```python
Attributes:
    name (str): 사용자의 이름.
    age (int): 사용자의 나이.
```

---

## 5. Examples

### ✅ 의미

- 함수나 클래스의 **사용 예시**를 보여줄 때 사용합니다.
- 주로 코드 블록으로 구성됩니다.

### ✅ 예시

```python
Examples:
    >>> greet("Alice")
    'Hello, Alice!'
```

---

## ✅ 기타 섹션들 (선택적으로 사용)

| 섹션 이름       | 용도 예시          |
| ----------- | -------------- |
| `Note:`     | 중요한 참고 사항      |
| `Warning:`  | 경고할 내용         |
| `Todo:`     | 추후 작업 항목       |
| `See Also:` | 관련 함수나 문서 링크 등 |

---

## 📌 요약

- Google Style Docstring은 구조화된 문서 작성에 적합합니다.
- 주요 섹션은 `Args`, `Returns`, `Raises`, `Attributes`, `Examples`입니다.
- 일관된 스타일을 유지하면 자동 문서 생성 도구(Sphinx, pdoc 등)와 IDE의 도움을 더 잘 받을 수 있습니다.

