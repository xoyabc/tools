# 服务器基础监控优化
- 磁盘读写阈值如何定?
建议参考云服务磁盘应能值
```
腾讯云
普通云硬盘     随机IOPS：数百-100    吞吐量：40-100 MB/s
高性能云硬盘   随机IOPS：1500-4500   IOPS随容量变化公式：[1500+8*容量, max]  吞吐量：75-130 MB/s  吞吐量随容量变化公式：[75+0.147*容量, max]
SSD云硬盘     随机IOPS：2400-24000  IOPS随容量变化公式：[24*容量, max]      吞吐量：128-260 MB/s 吞吐量随容量变化公式：[128+0.147*(容量-100GB), max
```