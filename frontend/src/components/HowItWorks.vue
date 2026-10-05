<template>
  <section class="editorial-section steps-editorial-section">
    <div class="container">
      <div class="steps-editorial-layout">
        <!-- Left Side: Lead Headline -->
        <div class="steps-intro">
          <div class="header-kicker">
            <span class="editorial-label">Qadam-baqadam</span>
            <span class="editorial-tag">[ Yo'l xaritasi ]</span>
          </div>

          <h2 class="steps-headline">
            Ishtirok etish <span class="serif-italic-gold">bosqichlari</span> va g'oliblik sari <span class="serif-italic">yo'l</span>
          </h2>

          <p class="steps-lead-text">
            Olimpiadaga tayyorgarlik ko'rish va ishtirok etish uchun barcha jarayonlar sodda va shaffof tashkil etilgan.
          </p>
        </div>

        <!-- Right Side: Numbered Editorial Timeline -->
        <div class="steps-timeline">
          <div class="timeline-step">
            <span class="timeline-num">01</span>
            <div class="timeline-body">
              <h3 class="timeline-title">Onlayn ro'yxatdan o'tish</h3>
              <p class="timeline-desc">
                Sayt orqali ism-sharifingiz, telefon raqamingiz va sinfingizni kiritib o'rningizni band qiling.
              </p>
              <span class="editorial-tag">[ 1 daqiqa vaqt oladi ]</span>
            </div>
          </div>

          <div class="timeline-step">
            <span class="timeline-num">02</span>
            <div class="timeline-body">
              <h3 class="timeline-title">Olimpiada kuni va sinov</h3>
              <p class="timeline-desc">
                Belgilangan kuni Hackathon IT School binosiga keling va o'z bilim hamda mantiqiy mahoratingizni namoyon eting.
              </p>
              <span class="editorial-tag">[ Shaffof hakamlik ]</span>
            </div>
          </div>

          <div class="timeline-step">
            <span class="timeline-num">03</span>
            <div class="timeline-body">
              <h3 class="timeline-title">Natijalar va Taqdirlash</h3>
              <p class="timeline-desc">
                G'oliblar tantanali ravishda sertifikatlar, qimmatbaho esdalik sovg'alari va maxsus ta'lim imtiyozlari bilan taqdirlanadi.
              </p>
              <span class="editorial-tag text-gold">[ Sovg'alar va imtiyozlar ]</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>
.steps-editorial-section {
  background-color: var(--bg-section-1);
  position: relative;
}

.steps-editorial-layout {
  display: grid;
  grid-template-columns: 1fr 1.25fr;
  gap: 80px;
  align-items: start;
}

.steps-intro {
  position: sticky;
  top: 120px;
}

.header-kicker {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 20px;
}

.steps-headline {
  font-size: clamp(2.2rem, 3.8vw, 3.2rem);
  font-weight: 700;
  line-height: 1.15;
  letter-spacing: -0.03em;
  color: #ffffff;
  margin-bottom: 20px;
}

.steps-lead-text {
  font-size: 1.05rem;
  line-height: 1.7;
  color: var(--text-secondary);
}

/* Timeline */
.steps-timeline {
  display: flex;
  flex-direction: column;
  border-left: 1px solid var(--border-subtle);
  padding-left: 40px;
  gap: 48px;
}

.timeline-step {
  display: flex;
  gap: 28px;
  position: relative;
}

.timeline-num {
  font-family: var(--font-mono);
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--gold);
  line-height: 1;
}

.timeline-body {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.timeline-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #ffffff;
  letter-spacing: -0.01em;
}

.timeline-desc {
  font-size: 0.95rem;
  line-height: 1.65;
  color: var(--text-secondary);
  margin-bottom: 6px;
}

@media (max-width: 992px) {
  .steps-editorial-layout {
    grid-template-columns: 1fr;
    gap: 48px;
  }
  .steps-intro {
    position: static;
  }
  .steps-timeline {
    padding-left: 20px;
  }
}
</style>
