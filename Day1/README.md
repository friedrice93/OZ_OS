컴퓨터 하드웨어 구조
과제
1. CPU의 구성요소 ALU, CU, 그리고 레지스터 각각의 역할을 간략하게 정리해보자.

* CPU(Central Processing Unit)
 - 중앙 처리 장치, 컴퓨터 내부에서 주요 연산들을 처리하는 컴퓨터의 두뇌 역할을 수행하는 파트.
* ALU(Arithmetic Logic Unit)
 - 산술 논리 연산 장치.
 - 산술 연산(덧셈 뺄셈, 곱셈, 나눗셈 등)과 논리연산(AND, OR, NOT 등)을 수행.
 - ALU는 CPU가 데이터를 처리하고 계산하는 핵심 부분 . 중하나이며, 프로그램에서 수행되는 모든 연산은 ALU를 통해 이루어집니다.
* CU(Control Unit)
 - 제어 장치. 전체적인 컴퓨터 시스템의 동작을 제어하고 조정합니다.
 - CU는 CPU 내에서 명령어 해석, 실행 순서 관리, 입출력 장치와의 상호 작용, 그리고 다양한 기능을 수행합니다.
* Register
 - 고속 메모리 장치. 매우 빠른 속도로 데이터를 읽고 쓸 수 있는 작은 저장 공간.
 - CPU가 데이터를 저장하고 연산하는데 사용됩니다.
 - 주요 기능은 데이터 저장, 주소 지정, 임시 저장, 제어 정보 저장 등이 있습니다.

2. 메인 메모리와 보조기억장치의 차이를 간략하게 서술해보자.

* 속도
 - 메인 메모리 : 매우 빠른 엑세스 속도, 대부분의 메인 메모리는 RAM으로 구성, CPU에 직접 엑세스하여 빠르게 읽고 쓸 수 있음.
 - 보조기억장치 : 메인 메모리보다 훨씬 느린 속도, 하드 디스크 드라이브(HDD), 솔리스 스테이트 드라이브(SSD), 광학 디스크 등이 있음.
* 용량
 - 메인 메모리 : CPU가 직접 엑세스 하는 데이터의 일시적인 저장소로 상대적으로 작은 용량, 일반적으로 몇 기가바이트에서 몇 테라바이트.
 - 보조기억장치 : 대량의 데이터를 저장하는 데 사용, 하드 디스크 드라이브나 SSD는 수백 기가바이트에서 수십 테라바이트의 용량.
* 가격
 - 메인 메모리 : 비교적 비싼 가격, 용량이 증가할수록 가격도 비례적으로 증가.
 - 보조기억장치 : 메인 메모리보다 저렴한 가격에 더 많은 용량을 제공.
* 엑세스 방식
 - 메인 메모리 : CPU가 직접 엑세스 할 수 있는 공유 메모리.
 - 보조기억장치 : 일반적으로 데이터를 읽거나 쓰기 위해 CPU에 의해 명령을 내린 후에만 접근할 수 있음.

3. 버스 시스템은 데이터를 주고 받기 위한 경로로, 데이터의 종류에 따라 세 가지로 구분할 수 있다. 세 가지는 무엇인지 말해보자.

* 데이터 버스(Data Bus)
 - 데이터 버스는 데이터를 전송하는데 사용됩니다. CPU, 메모리, 그리고 입출력 장치 사이에 데이터가 전송됩니다. 데이터 버스는 이진 형태로 표현괸 데이터를 전송합니다.
* 주소 버스(Address Bus)
 - 주소 버스는 메모리나 입출력 장치에 대한 주소 정보를 전송하는데 사용됩니다. CPU는 주소 버스를 통해 메모리에 접근하거나 입출력 장치를 선택합니다. 주소 버스는 일반적으로 데이터 버스보다 더 많은 비트를 가지고 있으며, 이는 주소 공간의 크기에 따라 결정됩니다.
* 제어 버스(Control Bus)
 - 제어 버스는 제어 신호를 전송하는데 사용됩니다. CPU와 다른 하드웨어 간에 데이터 전송이나 연산의 시작과 종료, 그리고 버스의 사용 권한을 조절하는데 사용됩니다. 일반적으로 제어 버스에서는 클럭 신호, 읽기/쓰기 신호, 인터럽트 신호 등이 포함됩니다.
 