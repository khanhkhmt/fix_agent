[![Banners](docs/images/banner1.png)](https://github.com/xinnan-tech/xiaozhi-esp32-server)

<h1 align="center">Dịch vụ Backend Xiaozhi (xiaozhi-esp32-server)</h1>

<p align="center">
Dự án này dựa trên lý thuyết và công nghệ trí tuệ nhân máy cộng sinh để phát triển hệ thống phần cứng và phần mềm cho thiết bị thông minh.<br/>
Cung cấp dịch vụ backend cho dự án phần cứng thông minh mã nguồn mở
<a href="https://github.com/78/xiaozhi-esp32">xiaozhi-esp32</a>.<br/>
Được triển khai bằng Python, Java, Vue dựa trên <a href="https://ccnphfhqs21z.feishu.cn/wiki/M0XiwldO9iJwHikpXD5cEx71nKh">giao thức truyền thông Xiaozhi</a>.<br/>
Hỗ trợ các giao thức MQTT+UDP, Websocket, điểm truy cập MCP, nhận dạng giọng nói và cơ sở tri thức.
</p>

<p align="center">
<a href="./docs/FAQ.md">Câu hỏi thường gặp</a>
· <a href="https://github.com/xinnan-tech/xiaozhi-esp32-server/issues">Báo cáo vấn đề</a>
· <a href="./README.md#%E9%83%A8%E7%BD%B2%E6%96%87%E6%A1%A3">Tài liệu triển khai</a>
· <a href="https://github.com/xinnan-tech/xiaozhi-esp32-server/releases">Nhật ký cập nhật</a>
</p>

<p align="center">
  <a href="./README.md"><img alt="Tệp README bản Trung Quốc giản thể" src="https://img.shields.io/badge/简体中文-DBEDFA"></a>
  <a href="./README_en.md"><img alt="README in English" src="https://img.shields.io/badge/English-DFE0E5"></a>
  <a href="./README_vi.md"><img alt="Tiếng Việt" src="https://img.shields.io/badge/Tiếng Việt-DFE0E5"></a>
  <a href="./README_de.md"><img alt="Deutsch" src="https://img.shields.io/badge/Deutsch-DFE0E5"></a>
  <a href="./README_pt_BR.md"><img alt="Português (Brasil)" src="https://img.shields.io/badge/Português (Brasil)-DFE0E5"></a>
  <a href="https://github.com/xinnan-tech/xiaozhi-esp32-server/releases">
    <img alt="GitHub Contributors" src="https://img.shields.io/github/v/release/xinnan-tech/xiaozhi-esp32-server?logo=docker" />
  </a>
  <a href="https://github.com/xinnan-tech/xiaozhi-esp32-server/blob/main/LICENSE">
    <img alt="GitHub pull requests" src="https://img.shields.io/badge/license-MIT-white?labelColor=black" />
  </a>
  <a href="https://github.com/xinnan-tech/xiaozhi-esp32-server">
    <img alt="stars" src="https://img.shields.io/github/stars/xinnan-tech/xiaozhi-esp32-server?color=ffcb47&labelColor=black" />
  </a>
</p>

<p align="center">
Dẫn đầu bởi đội ngũ Giáo sư Siyuan Liu (Đại học Công nghệ Nam Trung Quốc)
</br>
刘思源教授团队主导研发（华南理工大学）
</br>
<img src="./docs/images/hnlg.jpg" alt="华南理工大学" width="50%">
</p>

---

## Đối tượng phù hợp 👥

Dự án này yêu cầu sử dụng cùng với phần cứng ESP32. Nếu bạn đã mua phần cứng ESP32, đã thành công trong việc kết nối với dịch vụ backend do "Shrimp Guy" triển khai và muốn tự xây dựng dịch vụ backend `xiaozhi-esp32` riêng, thì dự án này rất phù hợp với bạn.

Muốn xem hiệu quả sử dụng? Hãy nhấp vào video 🎥

<table>
  <tr>
    <td>
        <a href="https://www.bilibili.com/video/BV1FMFyejExX" target="_blank">
         <picture>
           <img alt="Cảm nhận tốc độ phản hồi" src="docs/images/demo9.png" />
         </picture>
        </a>
    </td>
    <td>
        <a href="https://www.bilibili.com/video/BV1vchQzaEse" target="_blank">
         <picture>
           <img alt="Mẹo tối ưu tốc độ" src="docs/images/demo6.png" />
         </picture>
        </a>
    </td>
    <td>
        <a href="https://www.bilibili.com/video/BV1C1tCzUEZh" target="_blank">
         <picture>
           <img alt="Cảnh y tế phức tạp" src="docs/images/demo1.png" />
         </picture>
        </a>
    </td>
    <td>
        <a href="https://www.bilibili.com/video/BV1zUW5zJEkq" target="_blank">
         <picture>
           <img alt="Phát lệnh MQTT" src="docs/images/demo4.png" />
         </picture>
        </a>
    </td>
    <td>
        <a href="https://www.bilibili.com/video/BV1Exu3zqEDe" target="_blank">
         <picture>
           <img alt="Nhận dạng dấu vân tay giọng nói" src="docs/images/demo14.png" />
         </picture>
        </a>
    </td>
  </tr>
  <tr>
    <td>
        <a href="https://www.bilibili.com/video/BV1pNXWYGEx1" target="_blank">
         <picture>
           <img alt="Điều khiển công tắc thiết bị gia dụng" src="docs/images/demo5.png" />
         </picture>
        </a>
    </td>
    <td>
        <a href="https://www.bilibili.com/video/BV1ZQKUzYExM" target="_blank">
         <picture>
           <img alt="Điểm truy cập MCP" src="docs/images/demo13.png" />
         </picture>
        </a>
    </td>
    <td>
      <a href="https://www.bilibili.com/video/BV1TJ7WzzEo6" target="_blank">
         <picture>
           <img alt="Nhiệm vụ đa lệnh" src="docs/images/demo11.png" />
         </picture>
        </a>
    </td>
    <td>
        <a href="https://www.bilibili.com/video/BV1VC96Y5EMH" target="_blank">
         <picture>
           <img alt="Phát nhạc" src="docs/images/demo7.png" />
         </picture>
        </a>
    </td>
    <td>
        <a href="https://www.bilibili.com/video/BV1Z8XuYZEAS" target="_blank">
         <picture>
           <img alt="Plugin thời tiết" src="docs/images/demo8.png" />
         </picture>
        </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://www.bilibili.com/video/BV12J7WzBEaH" target="_blank">
         <picture>
           <img alt="Gián đoạn thời gian thực" src="docs/images/demo10.png" />
         </picture>
        </a>
    </td>
    <td>
      <a href="https://www.bilibili.com/video/BV1Co76z7EvK" target="_blank">
         <picture>
           <img alt="Chụp ảnh nhận dạng vật phẩm" src="docs/images/demo12.png" />
         </picture>
        </a>
    </td>
    <td>
        <a href="https://www.bilibili.com/video/BV1CDKWemEU6" target="_blank">
         <picture>
           <img alt="Âm sắc tùy chỉnh" src="docs/images/demo2.png" />
         </picture>
        </a>
    </td>
    <td>
        <a href="https://www.bilibili.com/video/BV12yA2egEaC" target="_blank">
         <picture>
           <img alt="Giao tiếp bằng tiếng Quảng Đông" src="docs/images/demo3.png" />
         </picture>
        </a>
    </td>
    <td>
        <a href="https://www.bilibili.com/video/BV17LXWYvENb" target="_blank">
         <picture>
           <img alt="Báo tin tức" src="docs/images/demo0.png" />
         </picture>
        </a>
    </td>
  </tr>
</table>

---

## CẢNH BÁO ⚠️

1. Dự án này là phần mềm nguồn mở, phần mềm này không có quan hệ hợp tác thương mại với bất kỳ nhà cung cấp API bên thứ ba nào (bao gồm nhưng không giới hạn ở nhận dạng giọng nói, mô hình lớn, tổng hợp giọng nói, v.v.) và không bảo đảm bất kỳ chất lượng dịch vụ hay an toàn tài chính nào của họ. Người dùng nên ưu tiên chọn nhà cung cấp có giấy phép kinh doanh liên quan, và đọc kỹ các thỏa thuận dịch vụ và chính sách bảo mật. Phần mềm này không lưu trữ bất kỳ khóa tài khoản nào, không tham gia vào luồng tài chính, và không chịu trách nhiệm về mất mát vốn nạp.

2. Các tính năng của dự án chưa hoàn thiện và chưa qua đánh giá an ninh mạng, xin đừng sử dụng trong môi trường sản xuất. Nếu bạn triển khai dự án trên môi trường công cộng để học hỏi, hãy đảm bảo thực hiện các biện pháp bảo vệ cần thiết.

---

## Tài liệu triển khai

![Banners](docs/images/banner2.png)

Dự án cung cấp hai cách triển khai, xin chọn phù hợp với nhu cầu cụ thể của bạn:

#### 🚀 Lựa chọn phương thức triển khai
| Phương thức triển khai | Đặc điểm | Kịch bản áp dụng | Tài liệu triển khai | Yêu cầu cấu hình | Video hướng dẫn |
|----------------------|----------|-------------------|-------------------|-------------------|-------------------|
| **Cài đặt tối giản** | Đàm thoại thông minh, quản lý một trí tuệ duy nhất | Môi trường cấu hình thấp, dữ liệu lưu trong tệp cấu hình, không cần cơ sở dữ liệu | ①Phiên bản Docker / ②Triển khai từ mã nguồn | Nếu dùng `FunASR`: 2 CPU + 4 GB RAM; nếu dùng toàn bộ API: 2 CPU + 2 GB RAM | - |
| **Cài đặt đầy đủ các mô‑đun** | Đàm thoại thông minh, quản lý đa người dùng, quản lý đa trí tuệ, giao diện bảng điều khiển | Trải nghiệm đầy đủ chức năng, dữ liệu lưu trong cơ sở dữ liệu | ①Phiên bản Docker / ②Triển khai từ mã nguồn / ③Hướng dẫn cập nhật tự động | Nếu dùng `FunASR`: 4 CPU + 8 GB RAM; nếu dùng toàn bộ API: 2 CPU + 4 GB RAM | Video hướng dẫn khởi động từ mã nguồn |

Các vấn đề thường gặp và hướng dẫn liên quan, có thể tham khảo [đây](./docs/FAQ.md)

> 💡 **Gợi ý:** Dưới đây là nền tảng thử nghiệm được triển khai bằng mã mới nhất, có thể ghi lại và thử nghiệm; đồng thời hỗ trợ 6 kết nối đồng thời, dữ liệu sẽ được xóa hàng ngày.

```
Địa chỉ bảng điều khiển: https://2662r3426b.vicp.fun
Bảng điều khiển (phiên bản H5): https://2662r3426b.vicp.fun/h5/index.html

Công cụ kiểm tra dịch vụ: https://2662r3426b.vicp.fun/test/
Địa chỉ giao diện OTA: https://2662r3426b.vicp.fun/xiaozhi/ota/
Địa chỉ giao diện Websocket: wss://2662r3426b.vicp.fun/xiaozhi/v1/
```

#### 🚩 Hướng dẫn cấu hình và đề xuất
> [!Note]
> Dự án này cung cấp hai giải pháp cấu hình:

> 1. **Bắt đầu hoàn toàn miễn phí**: Thích hợp cho sử dụng cá nhân, gia đình, tất cả các thành phần đều sử dụng gói miễn phí, không cần chi trả thêm.

> 2. **Cấu hình luồng**: Thích hợp cho các trường hợp trình diễn, đào tạo, hơn 2 kết nối đồng thời, áp dụng công nghệ xử lý luồng, tốc độ phản hồi nhanh hơn, trải nghiệm tốt hơn.

> Từ phiên bản `0.5.2` trở lên, dự án hỗ trợ cấu hình luồng, so với các phiên bản trước, tốc độ đáp ứng tăng khoảng **2,5 giây**, cải thiện đáng kể trải nghiệm người dùng.

| Tên mô‑đun | Cài đặt Bắt đầu miễn phí | Cấu hình luồng |
|:---:|:---:|:---:|
| ASR (Nhận dạng giọng nói) | FunASR (cục bộ) | 👍XunfeiStreamASR (Xunfei luồng) |
| LLM (Mô hình ngôn ngữ lớn) | glm‑4‑flash (ZhiPu) | 👍qwen‑flash (Alibaba Baile) |
| VLLM (Mô hình thị giác) | glm‑4v‑flash (ZhiPu) | 👍qwen2.5‑vl‑3b‑instructh (Alibaba Baile) |
| TTS (Tổng hợp giọng nói) | ✅LinkeraiTTS (Lingxi luồng) | 👍HuoshanDoubleStreamTTS (Huoshán luồng) |
| Intent (Nhận dạng ý định) | function_call (gọi hàm) | function_call (gọi hàm) |
| Memory (Bộ nhớ) | mem_local_short (bộ nhớ ngắn hạn cục bộ) | mem_local_short (bộ nhớ ngắn hạn cục bộ) |

Nếu bạn quan tâm tới thời gian thực hiện của từng thành phần, hãy tham khảo **Báo cáo kiểm tra hiệu năng các thành phần Xiaozhi** và có thể thực hiện các bài kiểm tra tương tự trong môi trường của mình.

#### 🔧 Công cụ kiểm thử
Dự án cung cấp các công cụ sau để giúp bạn xác thực hệ thống và lựa chọn mô hình phù hợp:

| Tên công cụ | Vị trí | Cách dùng | Mô tả |
|:---:|:---|:---:|:---:|
| Công cụ kiểm thử tương tác âm thanh | `main > xiaozhi-server > test > test_page.html` | Mở trực tiếp bằng trình duyệt Chrome | Kiểm tra phát và nhận âm thanh, xác nhận xử lý âm thanh phía Python có hoạt động bình thường |
| Công cụ kiểm thử phản hồi mô hình | `main > xiaozhi-server > performance_tester.py` | Chạy `python performance_tester.py` | Kiểm tra tốc độ phản hồi của các core module: ASR, LLM, VLLM, TTS |

> 💡 **Lưu ý:** Khi kiểm tra tốc độ mô hình, chỉ những mô hình đã được cấu hình khóa API mới được kiểm tra.

---

## Danh sách tính năng ✨

### Đã thực hiện ✅

> **Xem sơ đồ kiến trúc cài đặt đầy đủ các mô-đun**
| Tính năng | Mô tả |
|:---:|:---|
| **Kiến trúc lõi** | Dựa trên cổng MQTT+UDP, WebSocket, máy chủ HTTP, cung cấp hệ thống quản lý và xác thực đầy đủ cho bảng điều khiển |
| **Giao tiếp bằng giọng nói** | Hỗ trợ ASR (nhận dạng giọng nói) luồng, TTS (tổng hợp giọng nói) luồng, VAD (phát hiện hoạt động giọng nói); hỗ trợ nhận dạng đa ngôn ngữ và xử lý âm thanh |
| **Nhận dạng dấu vân tay giọng nói** | Hỗ trợ đăng ký, quản lý và nhận dạng dấu vân tay giọng nói cho nhiều người dùng, xử lý song song với ASR, nhận dạng danh tính người nói ngay lập tức và truyền tới LLM để trả lời cá nhân hoá |
| **Đàm thoại thông minh** | Hỗ trợ đa LLM (mô hình ngôn ngữ lớn) để thực hiện đàm thoại thông minh |
| **Nhận thức thị giác** | Hỗ trợ đa VLLM (mô hình thị giác lớn) để thực hiện tương tác đa mô‑hình |
| **Nhận dạng ý định** | Hỗ trợ nhận dạng ý định qua mô hình lớn bên ngoài và gọi hàm tự động, cung cấp cơ chế xử lý ý định dạng plugin |
| **Hệ thống nhớ** | Hỗ trợ bộ nhớ ngắn hạn cục bộ, bộ nhớ qua giao diện mem0ai, PowerMem thông minh; có khả năng tóm tắt bộ nhớ |
| **Cơ sở tri thức** | Hỗ trợ RAGFlow, cho phép mô hình lớn quyết định khi nào cần truy vấn cơ sở tri thức trước khi trả lời |
| **Gọi công cụ** | Hỗ trợ giao thức IOT phía client, giao thức MCP phía client, giao thức MCP phía server, giao thức điểm truy cập MCP, hàm công cụ tùy chỉnh |
| **Phát lệnh** | Dựa vào giao thức MQTT, hỗ trợ phát lệnh MCP từ bảng điều khiển tới thiết bị ESP32 |
| **Bảng quản trị** | Cung cấp giao diện web quản trị, hỗ trợ quản lý người dùng, cấu hình hệ thống và thiết bị; giao diện hỗ trợ tiếng Trung giản thể, phồn thể, tiếng Anh |
| **Công cụ kiểm thử** | Cung cấp công cụ kiểm tra hiệu năng, công cụ kiểm tra mô hình thị giác và công cụ kiểm tra tương tác âm thanh |
| **Hỗ trợ triển khai** | Hỗ trợ triển khai bằng Docker và cài đặt cục bộ, cung cấp quản lý đầy đủ file cấu hình |
| **Hệ thống plugin** | Hỗ trợ mở rộng plugin chức năng, phát triển plugin tùy chỉnh và hot‑load plugin |

### Đang phát triển 🚧

Nếu muốn biết tiến độ phát triển cụ thể, hãy **nhấp vào đây**. Câu hỏi thường gặp và các hướng dẫn liên quan, có thể tham khảo [đây](./docs/FAQ.md)

Nếu bạn là nhà phát triển phần mềm, đây là một **Thư công khai cho các nhà phát triển**, rất hoan nghênh sự tham gia!

---

## Hệ sinh thái sản phẩm 👬

Xiaozhi là một hệ sinh thái; khi bạn sử dụng sản phẩm này, cũng có thể xem các dự án xuất sắc khác trong hệ sinh thái này:  
[Những dự án mở nguồn liên quan](https://github.com/78/xiaozhi-esp32/blob/main/README_zh.md#%E7%9B%B8%E5%85%B3%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE)

---

## Danh sách nền tảng/thành phần được hỗ trợ 📋

### Mô hình ngôn ngữ LLM

| Cách sử dụng | Nền tảng hỗ trợ | Nền tảng miễn phí |
|:---:|:---:|:---:|
| Gọi API OpenAI | 阿里百炼、火山引擎、DeepSeek、智谱、Gemini、科大讯飞 | 智谱、Gemini |
| Gọi API Ollama | Ollama | - |
| Gọi API Dify | Dify | - |
| Gọi API Fastgpt | Fastgpt | - |
| Gọi API Coze | Coze | - |
| Gọi API Xinference | Xinference | - |
| Gọi API HomeAssistant | HomeAssistant | - |

Thực tế, bất kỳ LLM nào hỗ trợ giao thức OpenAI đều có thể tích hợp.

---  

### Mô hình thị giác VLLM

| Cách sử dụng | Nền tảng hỗ trợ | Nền tảng miễn phí |
|:---:|:---:|:---:|
| Gọi API OpenAI | 阿里百炼、智谱ChatGLMVLLM | 智谱ChatGLMVLLM |

Thực tế, bất kỳ VLLM nào hỗ trợ giao thức OpenAI đều có thể tích hợp.

---  

### TTS (Tổng hợp giọng nói)

| Cách sử dụng | Nền tảng hỗ trợ | Nền tảng miễn phí |
|:---:|:---:|:---:|
| Gọi API | EdgeTTS、科大讯飞、火山引擎、腾讯云、阿里云及百炼、CosyVoiceSiliconflow、TTS302AI、CozeCnTTS、GizwitsTTS、ACGNTTS、OpenAITTS、灵犀流式TTS、MinimaxTTS | 灵犀流式TTS、EdgeTTS、CosyVoiceSiliconflow(部分) |
| Dịch vụ cục bộ | FishSpeech、GPT_SOVITS_V2、GPT_SOVITS_V3、Index‑TTS、PaddleSpeech | Index‑TTS、PaddleSpeech、FishSpeech、GPT_SOVITS_V2、GPT_SOVITS_V3 |

---  

### VAD (Phát hiện hoạt động giọng nói)

| Loại | Tên nền tảng | Cách sử dụng | Mô hình phí | Ghi chú |
|:---:|:-----------:|:------------:|:-----------:|:------:|
| VAD | SileroVAD | Sử dụng cục bộ | Miễn phí | - |

---  

### ASR (Nhận dạng giọng nói)

| Cách sử dụng | Nền tảng hỗ trợ | Nền tảng miễn phí |
|:---:|:---:|:---:|
| Sử dụng cục bộ | FunASR、SherpaASR | FunASR、SherpaASR |
| Gọi API | FunASRServer、火山引擎、科大讯飞、腾讯云、阿里云、百度云、OpenAI ASR | FunASRServer |

---  

### Voiceprint (Nhận dạng dấu vân tay giọng nói)

| Cách sử dụng | Nền tảng hỗ trợ | Nền tảng miễn phí |
|:---:|:---:|:---:|
| Sử dụng cục bộ | 3D‑Speaker | 3D‑Speaker |

---  

### Memory (Lưu trữ bộ nhớ)

| Loại | Tên nền tảng | Cách sử dụng | Mô hình phí | Ghi chú |
|:------:|:---------------:|:----:|:-----------:|:------:|
| Memory | mem0ai | Gọi API | 1000 lần/tháng | - |
| Memory | powermem | Tổng kết cục bộ | Phụ thuộc vào LLM và DB | OceanBase mở source, hỗ trợ tìm kiếm thông minh |
| Memory | mem_local_short | Tổng kết cục bộ | Miễn phí | - |
| Memory | nomem | Chế độ không nhớ | Miễn phí | - |

---  

### Intent (Nhận dạng ý định)

| Loại | Tên nền tảng | Cách sử dụng | Mô hình phí | Ghi chú |
|:------:|:-------------:|:----:|:----------:|:---------------------:|
| Intent | intent_llm | Gọi API | Tùy theo LLM | Nhận dạng ý định qua mô hình lớn, tính đa dụng cao |
| Intent | function_call | Gọi API | Tùy theo LLM | Hoàn thành ý định qua gọi hàm mô hình lớn, tốc độ nhanh, hiệu quả tốt |
| Intent | nointent | Không nhận dạng | Miễn phí | Bỏ qua nhận dạng ý định, trả về kết quả đối thoại trực tiếp |

---  

### Rag (Truy xuất tăng cường)

| Loại | Tên nền tảng | Cách sử dụng | Mô hình phí | Ghi chú |
|:------:|:-------------:|:----:|:----------:|:---------------------:|
| Rag | ragflow | Gọi API | Tùy theo token tiêu thụ cho đoạn cắt & phân tích | Tận dụng khả năng truy xuất‑tăng cường của RagFlow để cung cấp câu trả lời chính xác hơn |

---  

## Lời cảm ơn 🙏

| Logo | Dự án/Công ty | Mô tả |
|:---:|:---:|:---|
| <img src="./docs/images/logo_bailing.png" width="160"> | **Bailing – Robot Đàm thoại Giọng nói** |
|  | Dự án này được truyền cảm hứng từ robot đàm thoại giọng nói Bailing và được thực hiện dựa trên nền tảng đó |
| <img src="./docs/images/logo_tenclass.png" width="160"> | **Tenclass** |
|  | Cảm ơn Tenclass đã thiết lập giao thức truyền thông tiêu chuẩn, giải pháp đa thiết bị tương thích và minh chứng thực tiễn cho các trường hợp tải cao trong hệ sinh thái Xiaozhi; cung cấp tài liệu kỹ thuật toàn chuỗi cho dự án |
| <img src="./docs/images/logo_xuanfeng.png" width="160"> | **Xuanfeng Technology** |
|  | Cảm ơn Xuanfeng Technology vì đã đóng góp khung gọi hàm, giao thức MCP và cơ chế gọi plugin; nhờ hệ thống chỉ lệnh chuẩn hoá và khả năng mở rộng động, nâng cao đáng kể hiệu suất tương tác và tính mở rộng của thiết bị IoT phía trước |
| <img src="./docs/images/logo_junsen.png" width="160"> | **huangjunsen** |
|  | Cảm ơn huangjunsen vì đã đóng góp module `Bảng điều khiển di động`, thực hiện kiểm soát và tương tác thời gian thực hiệu quả trên thiết bị di động đa nền tảng, nâng cao đáng kể tính tiện lợi và hiệu quả quản lý trong các kịch bản di động |
| <img src="./docs/images/logo_huiyuan.png" width="160"> | **Huìyuǎn Design** |
|  | Cảm ơn Huìyuǎn Design vì đã cung cấp giải pháp thị giác chuyên nghiệp cho dự án, với kinh nghiệm thực tiễn thiết kế cho hơn một ngàn doanh nghiệp, nâng cao trải nghiệm người dùng cho sản phẩm |
| <img src="./docs/images/logo_qinren.png" width="160"> | **Xi'an Qínrén Information Technology** |
|  | Cảm ơn Xi'an Qínrén Information Technology vì đã củng cố hệ thống thị giác của dự án, đảm bảo tính nhất quán và mở rộng của phong cách thiết kế trong nhiều kịch bản |
| <img src="./docs/images/logo_contributors.png" width="160"> | **Người đóng góp mã** |
|  | Cảm ơn tất cả các đóng góp viên, sự đóng góp của các bạn khiến dự án trở nên mạnh mẽ và bền vững hơn |

<a href="https://star-history.com/#xinnan-tech/xiaozhi-esp32-server&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=xinnan-tech/xiaozhi-esp32-server&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=xinnan-tech/xiaozhi-esp32-server&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=xinnan-tech/xiaozhi-esp32-server&type=Date" />
 </picture>
</a>

# oriagent-device
# oriagent-device