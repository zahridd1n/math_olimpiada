<template>
  <section class="editorial-hero">
    <!-- Mathematical Subtle Curves Background -->
    <div class="math-curves-bg" aria-hidden="true">
      <svg class="math-curves-svg animated-wave-1" viewBox="0 0 1440 900" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M-100 450 C 300 200, 600 700, 1000 350 C 1250 150, 1400 500, 1600 400" stroke="rgba(229, 178, 46, 0.12)" stroke-width="1.5" />
        <path d="M-50 550 C 350 300, 700 800, 1100 450 C 1300 250, 1450 600, 1650 500" stroke="rgba(147, 197, 253, 0.08)" stroke-width="1" />
      </svg>
      <svg class="math-curves-svg animated-wave-2" viewBox="0 0 1440 900" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M-100 650 C 400 400, 750 900, 1150 550 C 1350 350, 1500 700, 1700 600" stroke="rgba(192, 132, 252, 0.07)" stroke-width="1.2" stroke-dasharray="4 8" />
        <path d="M0 300 Q 400 100 800 400 T 1600 300" stroke="rgba(229, 178, 46, 0.06)" stroke-width="1" />
      </svg>
    </div>

    <div class="container">
      <div class="hero-editorial-layout">
        <!-- Main Editorial Content -->
        <div class="hero-text-block">
          <div class="hero-kicker-line">
            <span class="editorial-label">Hackathon IT School Taqdim Etadi</span>
            <span class="editorial-dot">•</span>
            <span class="editorial-tag">5–8-sinf o'quvchilari uchun</span>
          </div>

          <h1 class="hero-headline">
            Mantiqingni <span class="serif-italic-gold reveal-italic">sinovdan</span> o'tkaz va yangi iqtidoringni <span class="serif-italic reveal-italic">kashf et.</span>
          </h1>

          <p class="hero-paragraph">
            Farg'ona viloyati bo'yicha yosh matematiklar va bo'lajak IT mutaxassislari uchun 
            shaffof, nufuzli bellashuv. Quruq formulalar emas — intellektual salohiyat, tahliliy tafakkur va ta'lim grantlari.
          </p>

          <!-- Hero Action Buttons -->
          <div class="hero-actions-wrap">
            <router-link to="/register" class="btn-editorial-pill hero-cta-btn">
              <span>Ro'yxatdan o'tish</span>
              <span class="arrow-glyph">→</span>
            </router-link>

            <a href="#about" class="btn-secondary-hero">
              <span>Batafsil ma'lumot</span>
            </a>
          </div>
        </div>

        <!-- Editorial Visual Frame (Clean, authentic candid capture) -->
        <div class="hero-media-block">
          <div class="editorial-frame">
            <img 
              :src="heroImg || defaultHero" 
              alt="Hackathon IT School o'quvchilari mashg'ulot jarayonida" 
              class="editorial-image"
            />
            <div class="frame-caption-strip">
              <span class="editorial-tag">[ Rasmiy olimpiada 2025/2026 ]</span>
              <span class="editorial-tag">Farg'ona HQ</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Minimalist Editorial Data Row -->
      <div class="editorial-stats-row">
        <div class="stat-cell">
          <span class="stat-number-mono">500<span class="stat-sup">+</span></span>
          <span class="stat-caption">Ishtirok etgan o'quvchilar</span>
        </div>
        <div class="stat-cell">
          <span class="stat-number-mono">14</span>
          <span class="stat-caption">Shahar va tuman qamrovi</span>
        </div>
        <div class="stat-cell">
          <span class="stat-number-mono">100<span class="stat-sup">%</span></span>
          <span class="stat-caption">Shaffof va xolis hakamlik</span>
        </div>
        <div class="stat-cell">
          <span class="stat-number-mono text-gold">Grant</span>
          <span class="stat-caption">G'oliblarga ta'lim imtiyozi</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getSiteSettings } from '../services/api.js'
import defaultHero from '../assets/hero-students.jpg'

const heroImg = ref('')

onMounted(async () => {
  const settings = await getSiteSettings()
  if (settings && settings.hero_image_url) {
    heroImg.value = settings.hero_image_url
  }
})
</script>

<style scoped>
.editorial-hero {
  position: relative;
  min-height: 88vh;
  padding: calc(var(--header-height) + 50px) 0 80px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  background-color: var(--bg-deep);
  overflow: hidden;
}

.hero-editorial-layout {
  position: relative;
  z-index: 2;
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  align-items: center;
  gap: 70px;
  margin-bottom: 70px;
}

/* Kicker */
.hero-kicker-line {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 24px;
}

.editorial-dot {
  color: var(--text-dim);
  font-size: 0.8rem;
}

/* Headline */
.hero-headline {
  font-size: clamp(2.4rem, 4.2vw, 3.8rem);
  font-weight: 700;
  line-height: 1.12;
  letter-spacing: -0.035em;
  color: #ffffff;
  margin-bottom: 24px;
  max-width: 720px;
}

.hero-paragraph {
  font-size: 1.1rem;
  line-height: 1.7;
  color: var(--text-secondary);
  max-width: 580px;
  margin-bottom: 38px;
  font-weight: 400;
}

/* Hero Action Buttons */
.hero-actions-wrap {
  display: flex;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
}

.hero-cta-btn {
  height: 52px;
  padding: 0 32px;
  font-size: 1rem;
  box-shadow: 0 6px 25px rgba(229, 178, 46, 0.3);
}

.arrow-glyph {
  font-family: var(--font-sans);
  font-size: 1.1rem;
  transition: transform 0.2s ease;
}

.btn-editorial-pill:hover .arrow-glyph {
  transform: translateX(4px);
}

.btn-secondary-hero {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 52px;
  padding: 0 26px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-medium);
  color: #ffffff;
  font-size: 0.95rem;
  font-weight: 500;
  text-decoration: none;
  transition: all 0.25s ease;
  backdrop-filter: blur(8px);
}

.btn-secondary-hero:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: var(--border-light);
  color: var(--gold);
  transform: translateY(-1px);
}

/* Media Block */
.hero-media-block {
  display: flex;
  justify-content: flex-end;
}

.editorial-frame {
  position: relative;
  width: 100%;
  max-width: 440px;
  border-radius: 12px;
  overflow: hidden;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid var(--border-subtle);
}

.editorial-image {
  width: 100%;
  height: 420px;
  object-fit: cover;
  display: block;
  filter: contrast(1.02) saturate(1.05);
}

.frame-caption-strip {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 18px;
  background: rgba(7, 9, 19, 0.9);
  border-top: 1px solid var(--border-subtle);
}

/* Stats Row */
.editorial-stats-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 32px;
  padding-top: 40px;
  border-top: 1px solid var(--border-subtle);
}

.stat-cell {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.stat-number-mono {
  font-family: var(--font-mono);
  font-size: 2.3rem;
  font-weight: 700;
  letter-spacing: -0.04em;
  color: #ffffff;
  line-height: 1;
}

.stat-sup {
  font-size: 1.4rem;
  color: var(--gold);
  margin-left: 2px;
}

.stat-caption {
  font-size: 0.85rem;
  color: var(--text-secondary);
  font-weight: 400;
}

/* Responsive */
@media (max-width: 992px) {
  .hero-editorial-layout {
    grid-template-columns: 1fr;
    gap: 48px;
  }
  .hero-media-block {
    justify-content: flex-start;
  }
  .editorial-stats-row {
    grid-template-columns: repeat(2, 1fr);
    gap: 28px;
  }
}

@media (max-width: 600px) {
  .hero-headline {
    font-size: 2.1rem;
  }
  .quick-reg-box {
    flex-direction: column;
    padding: 12px;
    border-radius: 16px;
    gap: 12px;
  }
  .btn-editorial-pill {
    width: 100%;
    justify-content: center;
  }
  .editorial-image {
    height: 300px;
  }
}
</style>
