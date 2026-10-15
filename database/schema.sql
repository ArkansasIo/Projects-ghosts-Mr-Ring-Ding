CREATE DATABASE IF NOT EXISTS ringding CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE ringding;

CREATE TABLE IF NOT EXISTS memories (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  session_id VARCHAR(128) NOT NULL,
  role ENUM('system','user','assistant') NOT NULL,
  content LONGTEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX idx_memory_session_created (session_id, created_at)
);

CREATE TABLE IF NOT EXISTS dictionary (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  word VARCHAR(128) NOT NULL UNIQUE,
  definition TEXT,
  part_of_speech VARCHAR(64),
  example_sentence TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS quotes (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  identity_id BIGINT UNSIGNED NULL,
  category VARCHAR(64) NOT NULL,
  quote_text TEXT NOT NULL,
  animation_trigger VARCHAR(64),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS identities (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  code VARCHAR(32) NOT NULL UNIQUE,
  name VARCHAR(128) NOT NULL,
  role_name VARCHAR(128),
  appearance TEXT,
  voice_style TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS world_objects (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  object_key VARCHAR(128) NOT NULL UNIQUE,
  object_type VARCHAR(64) NOT NULL,
  state_json JSON NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS generated_text (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  kind ENUM('sentence','paragraph','response') NOT NULL,
  prompt TEXT NOT NULL,
  content LONGTEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE quotes ADD CONSTRAINT fk_quotes_identity
  FOREIGN KEY (identity_id) REFERENCES identities(id)
  ON DELETE SET NULL;

INSERT IGNORE INTO identities(code, name, role_name, appearance, voice_style) VALUES
('RID-001','Ring-A-Ding','Primary cartoon persona','Blue theatrical cartoon figure with elastic motion.','Energetic, playful, expressive.'),
('RID-002','The Blue Host','Friendly presenter','Bright blue with a wide smile and welcoming gestures.','Warm and conversational.'),
('RID-003','Bellstorm','Excited adventure identity','Rapid squash-and-stretch animation.','Fast, enthusiastic, comedic.'),
('RID-004','The Backdrop Keeper','World interaction identity','Blue figure with a glowing scene-control pointer.','Curious and theatrical.'),
('RID-005','Professor Ring','Teaching identity','Round spectacles and notebook.','Patient and explanatory.'),
('RID-006','Captain Ding','Adventure/game identity','Cartoon captain outfit.','Confident and upbeat.'),
('RID-007','Night Ring','Storytelling identity','Deep-blue silhouette with soft highlights.','Calm and atmospheric.'),
('RID-008','Circuit Ding','AI/technology identity','Blue figure with animated circuit patterns.','Precise and analytical.');
