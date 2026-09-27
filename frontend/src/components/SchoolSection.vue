<template>
  <section id="maktab" class="editorial-section school-trust-section">
    <div class="container">
      <div class="trust-grid">
        <!-- Left Side: Real Story & School Mission -->
        <div class="trust-story-col">
          <div class="header-kicker">
            <span class="editorial-label">Hackathon IT School Falsafasi</span>
            <span class="editorial-tag">[ Maktab haqida ]</span>
          </div>

          <h2 class="trust-heading">
            Kelajak IT yetakchilarini tayyorlaydigan <span class="serif-italic-gold">zamonaviy</span> <span class="serif-italic">ta'lim maskani</span>
          </h2>

          <p class="trust-description">
            Hackathon IT School — quruq nazariya emas, 100% amaliyot va mantiqiy fikrlashga tayanuvchi ta'lim dargohi. Biz o'quvchilarda faqat fanlarni o'rganishni emas, balki real muammolarga kreativ yechim topish va katta marralarni zabt etish ko'nikmasini shakllantiramiz.
          </p>

          <!-- Why Trust Us List -->
          <div class="trust-pillars">
            <div class="pillar-item">
              <div class="pillar-marker">01</div>
              <div class="pillar-info">
                <h4>Kuchli mentorlar va amaliy metodika</h4>
                <p>Olimpiada g'oliblari va amaliyotchi IT mutaxassislaridan jonli darslar.</p>
              </div>
            </div>

            <div class="pillar-item">
              <div class="pillar-marker">02</div>
              <div class="pillar-info">
                <h4>Grantlar va doimiy qo'llab-quvvatlash</h4>
                <p>Eng iqtidorli o'quvchilarga bepul ta'lim olish va nufuzli startap loyihalarda qatnashish imkoni.</p>
              </div>
            </div>

            <div class="pillar-item">
              <div class="pillar-marker">03</div>
              <div class="pillar-info">
                <h4>Xalqaro standartlar va musobaqalar</h4>
                <p>Faqat maktab dasturi bilan cheklanmay, xalqaro darajadagi algoritmik mantiq va dasturlash.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Side: Atmosphere Visual -->
        <div class="trust-visual-col">
          <div class="winner-showcase-card">
            <img 
              :src="schoolImg || defaultSchool" 
              alt="Hackathon IT School o'quv muhiti" 
              class="winner-photo"
            />
            
            <div class="winner-caption-overlay">
              <div class="caption-header">
                <span class="editorial-tag text-gold">[ HACKATHON TA'LIM ]</span>
                <span class="editorial-tag">Farg'ona</span>
              </div>
              <p class="caption-quote">
                "Bizning maqsadimiz — har bir yosh iqtidorga zamonaviy IT va matematika ko'nikmalarini chuqur o'rgatish."
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getSiteSettings } from '../services/api.js'
import defaultSchool from '../assets/winners.jpg'

const schoolImg = ref('')

onMounted(async () => {
  const settings = await getSiteSettings()
  if (settings && settings.school_image_url) {
    schoolImg.value = settings.school_image_url
  }
})
</script>

<style scoped>
.school-trust-section {
  background-color: var(--bg-section-3);
  position: relative;
}

.trust-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.95fr;
  align-items: center;
  gap: 70px;
}

.trust-story-col {
  display: flex;
  flex-direction: column;
}

.header-kicker {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 20px;
}

.trust-heading {
  font-size: clamp(2.2rem, 3.8vw, 3.2rem);
  font-weight: 700;
  line-height: 1.15;
  letter-spacing: -0.03em;
  color: #ffffff;
  margin-bottom: 20px;
}

.trust-description {
  font-size: 1.05rem;
  line-height: 1.7;
  color: var(--text-secondary);
  margin-bottom: 36px;
}

/* Pillars */
.trust-pillars {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.pillar-item {
  display: flex;
  align-items: flex-start;
  gap: 20px;
  padding: 18px 22px;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid var(--border-subtle);
  border-radius: 12px;
  transition: all 0.25s ease;
}

.pillar-item:hover {
  background: rgba(255, 255, 255, 0.04);
  border-color: rgba(229, 178, 46, 0.25);
}

.pillar-marker {
  font-family: var(--font-mono);
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--gold);
  background: rgba(229, 178, 46, 0.1);
  width: 38px;
  height: 38px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.pillar-info h4 {
  font-size: 1.02rem;
  font-weight: 600;
  color: #ffffff;
  margin-bottom: 4px;
}

.pillar-info p {
  font-size: 0.88rem;
  color: var(--text-secondary);
  line-height: 1.5;
  margin: 0;
}

/* Right Visual */
.trust-visual-col {
  display: flex;
  justify-content: center;
}

.winner-showcase-card {
  position: relative;
  width: 100%;
  max-width: 460px;
  border-radius: 14px;
  overflow: hidden;
  border: 1px solid var(--border-subtle);
}

.winner-photo {
  width: 100%;
  height: 480px;
  object-fit: cover;
  display: block;
}

.winner-caption-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 24px;
  background: linear-gradient(180deg, transparent 0%, rgba(6, 8, 20, 0.95) 30%, #060814 100%);
}

.caption-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
}

.caption-quote {
  font-family: var(--font-serif);
  font-style: italic;
  font-size: 0.95rem;
  color: #f1f5f9;
  line-height: 1.5;
  margin: 0;
}

@media (max-width: 992px) {
  .trust-grid {
    grid-template-columns: 1fr;
    gap: 48px;
  }
}
</style>
