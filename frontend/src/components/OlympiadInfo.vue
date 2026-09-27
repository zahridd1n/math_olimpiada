<template>
  <section id="olimpiada" class="editorial-section olympiad-spec-section">
    <div class="container">
      <div class="spec-layout">
        <!-- Left Side: Concept & Grade Categories -->
        <div class="spec-concept">
          <div class="header-kicker">
            <span class="editorial-label">Qoidalar & Nizom</span>
            <span class="editorial-tag">[ 02 ]</span>
          </div>

          <h2 class="spec-title">
            Olimpiada <span class="serif-italic-gold">formati</span> va ishtirok <span class="serif-italic">shartlari</span>
          </h2>

          <p class="spec-lead">
            Sinovlar 5–8-sinf o'quvchilari uchun 2 ta asosiy yosh toifasida alohida tuzilgan murakkablik darajasi asosida o'tkaziladi. Har bir bosqich mantiq, algoritmik fikrlash va noan'anaviy yondashuvni baholaydi.
          </p>

          <!-- Category Division -->
          <div class="grade-categories">
            <div class="grade-row">
              <span class="grade-level">5–6 SINF</span>
              <div class="grade-detail">
                <h4>Mantiq va boshlang'ich kombinatorika</h4>
                <p>Mantiqiy jumboqlar, sonlar qonuniyati, fazoviy tasavvur va nostandart masalalar.</p>
              </div>
            </div>

            <div class="grade-row">
              <span class="grade-level">7–8 SINF</span>
              <div class="grade-detail">
                <h4>Algebraik tahlil va geometrik tafakkur</h4>
                <p>Tenglamalar tizimi, geometrik isbotlar, mantiqiy algoritmlar va musobaqa masalalari.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Side: Official Editorial Specs Registry -->
        <div class="spec-registry">
          <div class="registry-sheet">
            <div class="sheet-top">
              <span class="editorial-tag">[ RASMIY MA'LUMOTNOMA ]</span>
              <span class="editorial-tag">2025/2026</span>
            </div>

            <div class="spec-entry">
              <span class="entry-label">Qabul muddati</span>
              <div class="entry-val-group">
                <span class="entry-val">{{ d.registrationDeadline }}</span>
                <span class="editorial-tag">[ Ro'yxat ochiq ]</span>
              </div>
            </div>

            <div class="spec-entry">
              <span class="entry-label">Olimpiada sanasi</span>
              <div class="entry-val-group">
                <span class="entry-val text-gold">{{ d.olympiadDate }}</span>
                <span class="editorial-tag">[ 1 kunlik asosiy bosqich ]</span>
              </div>
            </div>

            <div class="spec-entry">
              <span class="entry-label">O'tkazilish joyi</span>
              <div class="entry-val-group">
                <span class="entry-val">{{ d.location }}</span>
                <span class="editorial-tag">Farg'ona filiali</span>
              </div>
            </div>

            <div class="spec-entry">
              <span class="entry-label">Bosh tashkilotchi</span>
              <div class="entry-val-group">
                <span class="entry-val">{{ d.organizer }}</span>
              </div>
            </div>

            <div class="spec-entry">
              <span class="entry-label">Savollar va aloqa</span>
              <div class="entry-val-group">
                <span class="entry-val font-mono">{{ siteConfig.contact.phone }}</span>
                <span class="editorial-tag">Telegram & Call-center</span>
              </div>
            </div>

            <div class="sheet-bottom">
              <router-link to="/register" class="btn-editorial-pill w-full">
                <span>Olimpiadada ishtirok etish</span>
                <span>→</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { siteConfig } from '../config/site.js'
const d = siteConfig.olympiadDetails
</script>

<style scoped>
.olympiad-spec-section {
  background-color: var(--bg-section-3);
  position: relative;
}

.spec-layout {
  display: grid;
  grid-template-columns: 1.15fr 0.95fr;
  gap: 70px;
  align-items: start;
}

.spec-concept {
  display: flex;
  flex-direction: column;
}

.header-kicker {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 18px;
}

.spec-title {
  font-size: clamp(2.2rem, 3.8vw, 3.2rem);
  font-weight: 700;
  line-height: 1.15;
  letter-spacing: -0.03em;
  color: #ffffff;
  margin-bottom: 20px;
}

.spec-lead {
  font-size: 1.05rem;
  line-height: 1.7;
  color: var(--text-secondary);
  margin-bottom: 40px;
}

/* Categories */
.grade-categories {
  display: flex;
  flex-direction: column;
  border-top: 1px solid var(--border-subtle);
}

.grade-row {
  display: grid;
  grid-template-columns: 140px 1fr;
  padding: 24px 0;
  border-bottom: 1px solid var(--border-subtle);
  align-items: start;
  gap: 20px;
}

.grade-level {
  font-family: var(--font-mono);
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--gold);
  letter-spacing: 0.05em;
}

.grade-detail h4 {
  font-size: 1.05rem;
  font-weight: 600;
  color: #ffffff;
  margin-bottom: 4px;
}

.grade-detail p {
  font-size: 0.88rem;
  color: var(--text-secondary);
  line-height: 1.5;
  margin: 0;
}

/* Registry Sheet */
.registry-sheet {
  background: rgba(255, 255, 255, 0.025);
  border: 1px solid var(--border-medium);
  border-radius: 14px;
  padding: 36px;
  display: flex;
  flex-direction: column;
}

.sheet-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 24px;
  border-bottom: 1px solid var(--border-subtle);
  margin-bottom: 20px;
}

.spec-entry {
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding: 16px 0;
  border-bottom: 1px solid var(--border-subtle);
}

.entry-label {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--text-dim);
}

.entry-val-group {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 8px;
}

.entry-val {
  font-size: 1.05rem;
  font-weight: 600;
  color: #ffffff;
}

.sheet-bottom {
  padding-top: 28px;
}

.w-full {
  width: 100%;
  justify-content: center;
}

@media (max-width: 992px) {
  .spec-layout {
    grid-template-columns: 1fr;
    gap: 48px;
  }
}

@media (max-width: 600px) {
  .grade-row {
    grid-template-columns: 1fr;
    gap: 8px;
  }
  .registry-sheet {
    padding: 24px;
  }
}
</style>
